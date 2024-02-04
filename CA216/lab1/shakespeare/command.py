from cmd import Cmd
import os
class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
    
        print ("Hello, %s" % name)

    def do_dir(self, args):
        """Lists the files contained in the current working directory, supported commands:\n dir (path - optional) ls\n, dir (path - optional) ls -l\ndir (path - optional) ls -r\ndir (path - optional) ls -lR"""
        path = "."
        command = ""
        
        if len(args.split()) == 3:
            path = args.split()[0].strip()
            command = " ".join(args.split()[1:]).strip()
        elif len(args.split()) >= 2:
            command = " ".join(args.split()[0:]).strip()
        
        files = os.listdir(path)
        
        if not len(command) or command == "ls":
            for name in sorted(files):
                print(name)
        elif command == "ls -r":
            self.list_reverse(files)
    
    def list_reverse(self, files):
        for name in reversed(files):
            print(name)


    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit



if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')