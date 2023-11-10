import voicemeeterlib
import json

with open('temp/save.json', 'r') as f:
    data = json.load(f)

def main():
    with voicemeeterlib.api("potato") as vm:
        vm.apply(data)

if __name__ == "__main__":
    main()