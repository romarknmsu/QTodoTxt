from PySide import QtCore
from PySide import QtGui

from qtodotxt.ui.resource_manager import getIcon
from qtodotxt.ui.views import about_view

class MenuController(QtCore.QObject):
    def __init__(self, main_controller, menu):
        super(MenuController, self).__init__()
        self._main_controller = main_controller
        self._menu = menu
        self._initMenuBar()
            
    def _initMenuBar(self):
        self._initFileMenu()
        self._initEditMenu()
        self._initHelpMenu()
        
    def _initFileMenu(self):
        fileMenu = self._menu.addMenu('&File')
        fileMenu.addAction(self._createNewAction())     
        fileMenu.addAction(self._createOpenAction())        
        fileMenu.addAction(self._createSaveAction())
        fileMenu.addAction(self._createRevertAction())
        fileMenu.addSeparator()
        preferenceMenu = fileMenu.addMenu(getIcon('wrench.png'),'&Preferences')
        preferenceMenu.addAction(self._createPreferenceAction())
        fileMenu.addSeparator()
        fileMenu.addAction(self._createExitAction())
     
    def _initEditMenu(self):
        editMenu = self._menu.addMenu('&Edit')
        tlc = self._main_controller._tasks_list_controller
        editMenu.addAction(tlc.createTaskAction)
        editMenu.addAction(tlc.deleteSelectedTasksAction)
        editMenu.addAction(tlc.completeSelectedTasksAction)
        
    def _initHelpMenu(self):
        helpMenu = self._menu.addMenu('&Help')
        helpMenu.addAction(self._createAboutAction())
        
    def _createAboutAction(self):
        action = QtGui.QAction(getIcon('help.png'), '&About', self)
        action.triggered.connect(self._about)
        return action
    
    def _about(self):
        about_view.show(self._menu)
        
    def _createNewAction(self):
        action = QtGui.QAction(getIcon('page.png'), '&New', self)
	# infrequent action, I prefer to use ctrl+n for new task.
        action.setShortcuts(["Ctrl+Shift+N"])
        action.triggered.connect(self._main_controller.new)
        return action
    
    def _createOpenAction(self):
        action = QtGui.QAction(getIcon('folder.png'), '&Open', self)
        action.setShortcuts(["Ctrl+O"])
        action.triggered.connect(self._main_controller.open)
        return action

    def _createSaveAction(self):
        action = QtGui.QAction(getIcon('disk.png'), '&Save', self)
        action.setShortcuts(["Ctrl+S"])
        action.triggered.connect(self._main_controller.save)
        self.saveAction = action
        return action

    def _createRevertAction(self):
        action = QtGui.QAction(getIcon('arrow_rotate_clockwise.png'), '&Revert', self)
        action.triggered.connect(self._main_controller.revert)
        self.revertAction = action
        return action

    def _createPreferenceAction(self):
        action = QtGui.QAction('Add created date', self,checkable=True)
        action.triggered.connect(self._main_controller.createdDate)
        self.prefAction = action
        return action

    def changeCreatedDateState(self,value=False):
        self.prefAction.setChecked(value)

    def _createExitAction(self):
        action = QtGui.QAction(getIcon('door_in.png'), 'E&xit', self)
        action.setShortcuts(["Alt+F4"])
        action.triggered.connect(self._main_controller.exit)
        return action
    
