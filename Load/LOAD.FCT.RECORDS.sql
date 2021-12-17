--======================================================================
--==	PREPARE DATABASE FOR PROCEDURE
--======================================================================
CREATE SCHEMA IF NOT EXISTS admin;
DROP PROCEDURE IF EXISTS admin.load_fct_records;

CREATE PROCEDURE admin.load_fct_records()
LANGUAGE SQL
AS
$$

    DO
    $DO$
    BEGIN
    IF NOT EXISTS ( ( SELECT * FROM information_schema.tables WHERE table_schema = 'fct' AND table_name = 'records' )) THEN
        RAISE INFO 'Table does not exist';
    ELSE

        --======================================================================
        --==   LOAD FCT.RECORDS TABLE WITH RAW.NANO RECORDS
        --======================================================================
        INSERT INTO fct.records (
        device_id ,property_id ,value ,time_stamp ,batch_date) SELECT 
        device_id ,property_id ,value ,time_stamp ,batch_date  FROM raw.nano;

    END IF;
    END;
    $DO$

$$
