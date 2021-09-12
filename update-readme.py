from simpledemotivators import Demotivator
import subprocess


demotivator = Demotivator('его идеи', 'будут актуальны всегда')
demotivator.create('https://github.com/kylichist.png?size=460', url=True, RESULT_FILENAME='main_pic.png', delete_file=True, arrange=True)
subprocess.run(['git', 'commit', '-a', '-m', 'Update README.md'])
subprocess.run(['git', 'push'])
