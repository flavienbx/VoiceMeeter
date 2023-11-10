import voicemeeterlib
import json

class Param:
    strip = ["strip-0", "strip-1", "strip-2", "strip-3", "strip-4", "strip-5", "strip-6", "strip-7"]
    option_strip = ["label", "gain", "A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "mono", "solo", "mute", "audibility", "limit", "bass", "mid", "treble", "reverb", "delay", "fx1", "fx2", "pan_x", "pan_y", "color_x", "color_y", "fx_x", "fx_y", "postreverb", "postdelay", "postfx1", "postfx2", "comp", "comp.knob", "comp.gainin", "comp.ratio", "comp.threshold", "comp.attack", "comp.release", "comp.knee", "comp.gainout", "comp.makeup", "gate", "gate.knob", "gate.threshold", "gate.damping", "gate.bpsidechain", "gate.attack", "gate.hold", "gate.release", "denoiser"]
    bus = ["bus-0", "bus-1", "bus-2", "bus-3", "bus-4", "bus-5", "bus-6", "bus-7"]
    option_bus = ["mono", "mute", "sel", "gain", "label", "returnreverb", "returndelay", "returnfx1", "returnfx2", "monitor"]

def main(): 
    with voicemeeterlib.api("potato") as vm:
        data = {}
        for x in Param.strip:
            data[x] = {}
            id = int(Param.strip.index(x))
            for y in Param.option_strip:
                try:
                    if y == "label":
                        data[x][y] = vm.strip[id].label
                    elif y == "gain":
                        data[x][y] = vm.strip[id].gain
                    elif y == "A1":
                        data[x][y] = vm.strip[id].A1
                    elif y == "A2":
                        data[x][y] = vm.strip[id].A2
                    elif y == "A3":
                        data[x][y] = vm.strip[id].A3
                    elif y == "A4":
                        data[x][y] = vm.strip[id].A4
                    elif y == "A5":
                        data[x][y] = vm.strip[id].A5
                    elif y == "B1":
                        data[x][y] = vm.strip[id].B1
                    elif y == "B2":
                        data[x][y] = vm.strip[id].B2
                    elif y == "B3":
                        data[x][y] = vm.strip[id].B3
                    elif y == "mono":
                        data[x][y] = vm.strip[id].mono
                    elif y == "solo":
                        data[x][y] = vm.strip[id].solo
                    elif y == "mute":
                        data[x][y] = vm.strip[id].mute
                    elif y == "audibility":
                        data[x][y] = vm.strip[id].audibility
                    elif y == "limit":
                        data[x][y] = vm.strip[id].limit
                    elif y == "bass":
                        data[x][y] = vm.strip[id].bass
                    elif y == "mid":
                        data[x][y] = vm.strip[id].mid
                    elif y == "treble":
                        data[x][y] = vm.strip[id].treble
                    elif y == "reverb":
                        data[x][y] = vm.strip[id].reverb
                    elif y == "delay":
                        data[x][y] = vm.strip[id].delay
                    elif y == "fx1":
                        data[x][y] = vm.strip[id].fx1
                    elif y == "fx2":
                        data[x][y] = vm.strip[id].fx2
                    elif y == "pan_x":
                        data[x][y] = vm.strip[id].pan_x
                    elif y == "pan_y":
                        data[x][y] = vm.strip[id].pan_y
                    elif y == "color_x":
                        data[x][y] = vm.strip[id].color_x
                    elif y == "color_y":
                        data[x][y] = vm.strip[id].color_y
                    elif y == "fx_x":
                        data[x][y] = vm.strip[id].fx_x
                    elif y == "fx_y":
                        data[x][y] = vm.strip[id].fx_y
                    elif y == "postreverb":
                        data[x][y] = vm.strip[id].postreverb
                    elif y == "postdelay":
                        data[x][y] = vm.strip[id].postdelay
                    elif y == "postfx1":
                        data[x][y] = vm.strip[id].postfx1
                    elif y == "postfx2":
                        data[x][y] = vm.strip[id].postfx2
                    elif y == "comp":
                        data[x]['comp'] = vm.strip[id].comp.knob # Debug line not to delete
                        data[x]['comp'] = {}
                    elif y == "comp.knob":
                        data[x]['comp']['knob'] = vm.strip[id].comp.knob
                    elif y == "comp.gainin":
                        data[x]['comp']['gainin'] = vm.strip[id].comp.gainin
                    elif y == "comp.ratio":
                        data[x]['comp']['ratio'] = vm.strip[id].comp.ratio
                    elif y == "comp.threshold":
                        data[x]['comp']['threshold'] = vm.strip[id].comp.threshold
                    elif y == "comp.attack":
                        data[x]['comp']['attack'] = vm.strip[id].comp.attack
                    elif y == "comp.release":
                        data[x]['comp']['release'] = vm.strip[id].comp.release
                    elif y == "comp.knee":
                        data[x]['comp']['knee'] = vm.strip[id].comp.knee
                    elif y == "comp.gainout":
                        data[x]['comp']['gainout'] = vm.strip[id].comp.gainout
                    elif y == "comp.makeup":
                        data[x]['comp']['makeup'] = vm.strip[id].comp.makeup
                    elif y == "gate":
                        data[x]['gate'] = vm.strip[id].gate.knob # Debug line not to delete
                        data[x]['gate'] = {}
                    elif y == "gate.knob":
                        data[x]['gate']['knob'] = vm.strip[id].gate.knob
                    elif y == "gate.threshold":
                        data[x]['gate']['threshold'] = vm.strip[id].gate.threshold
                    elif y == "gate.damping":
                        data[x]['gate']['damping'] = vm.strip[id].gate.damping
                    elif y == "gate.bpsidechain":
                        data[x]['gate']['bpsidechain'] = vm.strip[id].gate.bpsidechain
                    elif y == "gate.attack":
                        data[x]['gate']['attack'] = vm.strip[id].gate.attack
                    elif y == "gate.hold":
                        data[x]['gate']['hold'] = vm.strip[id].gate.hold
                    elif y == "gate.release":
                        data[x]['gate']['release'] = vm.strip[id].gate.release
                    elif y == "denoiser":
                        data[x]['denoiser'] = vm.strip[id].denoiser.knob # Debug line not to delete
                        data[x]['denoiser'] = {}
                        data[x]['denoiser']['knob'] = vm.strip[id].denoiser.knob
                except:
                    pass
        for x in Param.bus:
            data[x] = {}
            id = int(Param.bus.index(x))
            for y in Param.option_bus:
                try:
                    if y == "mono":
                        data[x][y] = vm.bus[id].mono
                    elif y == "mute":
                        data[x][y] = vm.bus[id].mute
                    elif y == "sel":
                        data[x][y] = vm.bus[id].sel
                    elif y == "gain":
                        data[x][y] = vm.bus[id].gain
                    elif y == "label":
                        data[x][y] = vm.bus[id].label
                    elif y == "returnreverb":
                        data[x][y] = vm.bus[id].returnreverb
                    elif y == "returndelay":
                        data[x][y] = vm.bus[id].returndelay
                    elif y == "returnfx1":
                        data[x][y] = vm.bus[id].returnfx1
                    elif y == "returnfx2":
                        data[x][y] = vm.bus[id].returnfx2
                    elif y == "monitor":
                        data[x][y] = vm.bus[id].monitor
                except:
                    pass
    with open('temp/save.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()
    
