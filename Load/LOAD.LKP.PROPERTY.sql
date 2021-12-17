DO
$DO$
BEGIN
IF NOT EXISTS ( ( SELECT * FROM information_schema.tables WHERE table_schema = 'lkp' AND table_name = 'property' )) THEN
    RAISE INFO 'Table does not exist';
ELSE

        --======================================================================
        --==    LOAD LKP.PROPERTY WITH DEFINED PROPERTY VALUES
        --======================================================================
        INSERT INTO lkp.property
         (id    ,sensor_id ,name                      ,unit                ,version ,firmware) VALUES
         (23    ,12        ,'Temperature'             ,'C'                 ,'1'     ,'1.2.2')
        ,(24    ,12        ,'Relative Humidity'       ,'%'                 ,'1'     ,'1.2.2')
        ,(25    ,13        ,'PM 2.5'                  ,'ug/m^3'            ,'1'     ,'1.2.2')
        ,(26    ,13        ,'PM 10.0'                 ,'ug/m^3'            ,'1'     ,'1.2.2')
        ,(27    ,14        ,'Ozone'                   ,'PPB'               ,'1'     ,'1.2.2')
        ,(28    ,15        ,'Carbon Dioxide'          ,'PPM'               ,'1'     ,'1.2.2')
        ,(29    ,16        ,'Gas Resistance'          ,'ohms'              ,'1'     ,'1.2.2')
        ,(30    ,16        ,'Pressure'                ,'PA'                ,'1'     ,'1.2.2')
        ,(31    ,16        ,'Temperature'             ,'C'                 ,'1'     ,'1.2.2')
        ,(32    ,16        ,'Relative Humidity'       ,'%'                 ,'1'     ,'1.2.2')
        ,(33    ,16        ,'Indor Air Quality'       ,'Index'             ,'1'     ,'1.2.2')
        ,(34    ,17        ,'VOC Reducing Ration'     ,'Ration'            ,'1'     ,'1.2.2')
        ,(35    ,17        ,'Voc Oxidizing Ration'    ,'Ration'            ,'1'     ,'1.2.2')
        ,(36    ,17        ,'Ammonia Resistance'      ,'Ration'            ,'1'     ,'1.2.2');

END IF;
END;
$DO$
