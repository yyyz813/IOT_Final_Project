DO
$DO$
BEGIN
IF NOT EXISTS ( ( SELECT * FROM information_schema.tables WHERE table_schema = 'lkp' AND table_name = 'device' )) THEN
    RAISE INFO 'Table does not exist';
ELSE

        --======================================================================
        --==    LOAD LKP.DEVICE WITH AVAILABLE DEVICES
        --======================================================================
        INSERT INTO lkp.device
        (id    ,name             ,serial_number        ,active_status) VALUES
        (109   ,'Parkland 2'     ,'N/A'                ,1);

END IF;
END;
$DO$
