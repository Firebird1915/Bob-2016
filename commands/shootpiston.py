import wpilib
from wpilib.command import Command
from subsystems.pneumatics_comp import Pneumatics

class shoot_piston(Command):
    """
        Shoot piston off button trigger
    """
    def __init__(self, pneumatics_comp):
        super().__init__()

        self.setInterruptible(False)
        self.pneumatics_comp = pneumatics_comp
        self.requires(pneumatics_comp)
        self.setTimeout(1)

    def initialize(self):
        '''called before the command runs for the first time'''

    def execute(self):
        ''' Called repeatedly when the command is scheduled to run '''
        self.pneumatics_comp.shootball()
        self.pneumatics_comp.pullpistion()
        return self.setTimeout(0.9)

    def isFinished(self):
        return self.isTimedOut()