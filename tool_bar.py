from PyQt5.QtWidgets import QAction,qApp,QToolBar
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class ToolBar:

    def __init__(self,parent):
        toolbar = QToolBar(parent)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolbar.setIconSize(QSize(50,50))
        toolbar.set
        # icon_size = QSize()

        appointment = QAction(QIcon('./icons/schedule.png'), 'Appointment', parent)
        # appointment.setIconSize(QSize(50,50))
        appointment.setShortcut('Ctrl+F3')
        appointment.setStatusTip('Schedule an appointment')
        toolbar.addAction(appointment)

        op_register = QAction(QIcon('./icons/clinic.png'), 'OP Register', parent)
        op_register.setShortcut('Ctrl+F3')
        op_register.setStatusTip('Out-Patient register')
        toolbar.addAction(op_register)

        billing = QAction(QIcon('./icons/invoice.png'), 'Billing', parent)
        billing.setShortcut('Ctrl+F4')
        billing.setStatusTip('Billing')
        toolbar.addAction(billing)

        reports = QAction(QIcon('./icons/report.png'), 'Reports', parent)
        reports.setShortcut('Ctrl+F6')
        reports.setStatusTip('View Reports')
        toolbar.addAction(reports)

        lock = QAction(QIcon('./icons/lock.png'), 'Lock', parent)
        lock.setShortcut('Ctrl+F7')
        lock.setStatusTip('Lock')
        toolbar.addAction(lock)

        exit = QAction(QIcon('./icons/exit.png'), 'Exit', parent)
        exit.setShortcut('Ctrl+F8')
        exit.setStatusTip('Exit')
        toolbar.addAction(exit)

        parent.addToolBar(toolbar)


