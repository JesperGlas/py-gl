from mimetypes import init
import sys
import glfw

class Base:
    
    def __init__(self, window_title="GLFW Window", screen_size=(800, 600)):
        if not glfw.init():
            print("Failed to initialize GLFW...")
            return
        
        self._Window = glfw.create_window(
            screen_size[0], screen_size[1],
            window_title,
            None, None
        )
        
        if not self._Window:
            glfw.terminate()
            print("Failed to create GLFW window...")
            return

        # set current context as window
        glfw.make_context_current(self._Window)

    def update(self):
        pass
    
    def shutdown(self):
        glfw.terminate()
        sys.exit()

    def run(self):
        while not glfw.window_should_close(self._Window):

            # render
            self.update()
            glfw.swap_buffers(self._Window)
            
            # poll for events
            glfw.poll_events()
            
        self.shutdown()