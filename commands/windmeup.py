import wpilib
from wpilib.command import Command
from subsystems.intake import Intake

class WindMeUp(Command):
    """wind up motors on cue"""
    def __init__(self, intake):
        super().__init__()
        self.intake = intake
        self.requires(intake)

    def initialize(self):
        '''called before the command runs for the first time'''

    def execute(self):
        ''' Called repeatedly when the command is scheduled to run '''
        windup()
        wpilib.Wait(1.0)
        self.setTimeout(0)

    def isFinished(self):
        return self.isTimedOut()
