from com.snaplogic.scripting.language import ScriptHook
from com.snaplogic.scripting.language.ScriptHook import *
import base64 as base64

class TransformScript(ScriptHook):
    def __init__(self, input, output, error, log):
        self.input = input
        self.output = output
        self.error = error
        self.log = log

    def execute(self):
        self.log.info("Executing Transform script")
        i = 0
        while self.input.hasNext():
            data = self.input.next()
            filename = data['filename']
            with open(filename, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                self.log.info("Writing converted base64 string to output")
                self.output.write(encoded_string);
        self.log.info("Finished executing the Transform script")

hook = TransformScript(input, output, error, log)
