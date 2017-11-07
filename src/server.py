import serverclientsocket as scs
import json
import jsonalarms as ja
import jsonalarmsutils as jau

s = scs.ServerSocket()
a = ja.Alarms("alarms.json").load()

while True:
    jau.check_alarms(a)
    a.save()
    if s.msg is not None:
        try:
            alarms = json.loads(s.msg)
        except json.decoder.JSONDecodeError:
            pass
        else:
            print("Got JSON:", s.msg)
            a.save_new(alarms)
            a.load()
            s.msg = None

        if s.msg == "stop":
            jau.stop_trigger()
            s.msg = None
        elif s.msg == "quit":
            break
        else:
            s.msg = None