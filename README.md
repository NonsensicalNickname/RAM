<h1>Pyfirmata is sort of broken on 3.11, add the following:</h1>
<h6>        
        import inspect
            if not hasattr(inspect, 'getargspec'):
                inspect.getargspec = inspect.getfullargspec
</h6>
