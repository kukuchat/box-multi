FILE_HEADER = """<?xml version="1.0"?>
<tags>
    <tag>
        <name>n/a</name>
        <group>n/a</group>
        <resourceLocator>
            <protocolName>n/a</protocolName>
            <object_type>n/a</object_type>
            <device_id>n/a</device_id>
            <data_type>n/a</data_type>
            <arraysize>n/a</arraysize>
            <conversion>n/a</conversion>
            <object_instance>n/a</object_instance>
            <object_property>n/a</object_property>
            <array_index>n/a</array_index>
            <write_priority>n/a</write_priority>
            <cov>n/a</cov>
        </resourceLocator>
        <encoding>n/a</encoding>
        <refreshTime>n/a</refreshTime>
        <accessMode>n/a</accessMode>
        <active>n/a</active>
        <TAGLOCATOR>n/a</TAGLOCATOR>
        <comment>n/a</comment>
        <simulator>
            <DataSimulator>n/a</DataSimulator>
            <Amplitude>n/a</Amplitude>
            <Simulator_offset>n/a</Simulator_offset>
            <Period>n/a</Period>
        </simulator>
        <scaling>
            <enableScaling>n/a</enableScaling>
            <scalingType>n/a</scalingType>
            <enableLimits>n/a</enableLimits>
            <factors>
                <s1>n/a</s1>
                <s2>n/a</s2>
                <s3>n/a</s3>
                <tagS1>n/a</tagS1>
                <tagS2>n/a</tagS2>
                <tagS3>n/a</tagS3>
            </factors>
            <limits>
                <eumin>n/a</eumin>
                <eumax>n/a</eumax>
                <elmin>n/a</elmin>
                <elmax>n/a</elmax>
            </limits>
        </scaling>
        <decimalDigits>
            <ddTag>n/a</ddTag>
            <ddDigits>n/a</ddDigits>
        </decimalDigits>
        <castType>n/a</castType>
        <default>n/a</default>
        <min>n/a</min>
        <max>n/a</max>
        <statesText>n/a</statesText>
    </tag>
"""

TAG = """    <tag>
        <name>{d[name]}</name>
        <group>{d[group]}</group>
        <resourceLocator>
            <protocolName>BACN</protocolName>
            <object_type>{d[object_type]}</object_type>
            <device_id>{d[device_id]}</device_id>
            <data_type>{d[data_type]}</data_type>
            <arraysize></arraysize>
            <conversion></conversion>
            <object_instance>{d[object_instance]}</object_instance>
            <object_property>{d[object_property]}</object_property>
            <array_index>{d[array_index]}</array_index>
            <write_priority>{d[write_priority]}</write_priority>
            <cov>{d[cov]}</cov>
        </resourceLocator>
        <encoding></encoding>
        <refreshTime>{d[refresh_time]}</refreshTime>
        <accessMode>{d[access_mode]}</accessMode>
        <active>{d[active]}</active>
        <TAGLOCATOR></TAGLOCATOR>
        <comment>{d[comment]}</comment>
        <simulator>
            <DataSimulator>Variables</DataSimulator>
            <Amplitude></Amplitude>
            <Simulator_offset></Simulator_offset>
            <Period></Period>
        </simulator>
        <scaling>
            <enableScaling>false</enableScaling>
            <scalingType>byFormula</scalingType>
            <enableLimits>false</enableLimits>
            <factors>
                <s1>1</s1>
                <s2>1</s2>
                <s3>0</s3>
                <tagS1></tagS1>
                <tagS2></tagS2>
                <tagS3></tagS3>
            </factors>
            <limits>
                <eumin>0</eumin>
                <eumax>100</eumax>
                <elmin></elmin>
                <elmax></elmax>
            </limits>
        </scaling>
        <decimalDigits>
            <ddTag></ddTag>
            <ddDigits></ddDigits>
        </decimalDigits>
        <castType></castType>
        <default></default>
        <min>-3.40282e+38</min>
        <max>3.40282e+38</max>
        <statesText></statesText>
    </tag>
"""

FILE_FOOTER = """</tags>
"""
