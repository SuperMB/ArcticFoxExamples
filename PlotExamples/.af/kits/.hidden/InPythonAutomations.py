import clr
from System import *
from System.IO import *
from System.Collections.Generic import *
from System.Text import *
clr.AddReference('ArcticFox')
clr.AddReference('ArcticFoxBasic')
from ArcticFox import *
from ArcticFox.Public import *
from ArcticFox.Tokens import *
from ArcticFox.Tokens.Python import *
from ArcticFoxBasic import *
from ArcticFoxBasic.Automations import *
from ArcticFoxBasic.Automations.Python import *
from ArcticFox.Automations import *
clr.ImportExtensions(Functions)




class SetLeashToPlot(PythonAutomation):

    def ApplyAutomation(self):

        self.SetExamplePackage('plot')

        self.CodeAfterSeed += f"""
print('Leash set to plot')"""

