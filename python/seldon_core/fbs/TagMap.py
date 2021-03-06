# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class TagMap(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTagMap(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TagMap()
        x.Init(buf, n + offset)
        return x

    # TagMap
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TagMap
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TagMap
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def TagMapStart(builder): builder.StartObject(2)
def TagMapAddKey(builder, key): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(key), 0)
def TagMapAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def TagMapEnd(builder): return builder.EndObject()
