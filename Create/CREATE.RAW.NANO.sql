--======================================================================
--==	CREATE RAW.NANO TABLE FOR RAW DATA
--======================================================================
CREATE SCHEMA IF NOT EXISTS raw;
DROP TABLE IF EXISTS raw.nano;

CREATE TABLE raw.nano(
     device_id                   INT                            NOT NULL
    ,sensor_id                   INT                            NOT NULL
    ,property_id                 INT                            NOT NULL
    ,value                       FLOAT                          NOT NULL
    ,time_stamp                  TIMESTAMP WITH TIME ZONE
    ,batch_date                  TIMESTAMP WITH TIME ZONE
);

CREATE TRIGGER logged_actions
AFTER INSERT OR UPDATE OR DELETE ON raw.nano
    FOR EACH ROW EXECUTE PROCEDURE audit.if_modified_func();
