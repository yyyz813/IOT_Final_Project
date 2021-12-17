--======================================================================
--==	CREATE RAW.NANO TABLE FOR RAW DATA
--======================================================================
CREATE SCHEMA IF NOT EXISTS raw;
DROP TABLE IF EXISTS raw.synthetic;

CREATE TABLE raw.synthetic(
     device_id                   INT                            NOT NULL
    ,sensor_id                   INT                            NOT NULL
    ,property_id                 INT                            NOT NULL
    ,value                       FLOAT                          NOT NULL
    ,time_stamp                  TIMESTAMP WITH TIME ZONE       NOT NULL
    ,batch_date                  TIMESTAMP WITH TIME ZONE       NOT NULL
	  ,synthetic_data				       BOOLEAN						            NOT NULL
	  ,corrupt_data 				       BOOLEAN						            NOT NULL

);

CREATE TRIGGER logged_actions
AFTER INSERT OR UPDATE OR DELETE ON raw.synthetic
    FOR EACH ROW EXECUTE PROCEDURE audit.if_modified_func();