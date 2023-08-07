<h3>Pyfirmata is sort of broken on 3.11, add the following:
        
        import inspect
                if not hasattr(inspect, 'getargspec'):
                        inspect.getargspec = inspect.getfullargspec
</h3>
<h4>
        Instructions and other information.
</h4>
<p>
        Upload the code in StandardFirmata.txt to the arduino.
        Close the arduino software. Install dependencies for the python project.
        Apply the tweaks to the pyfirmata library as mentioned prior.
        Make any tweaks to RAM.py so that the angles mentioned in the comments in the first few lines match the fully down and fully up angles for your fingers. 
        Run the RAM.py python program. 
</p>
