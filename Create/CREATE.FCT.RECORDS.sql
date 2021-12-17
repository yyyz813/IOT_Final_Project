--======================================================================
--==   CREATE FCT.RECORDS FOR RECORD STORAGE
--======================================================================
CREATE SCHEMA IF NOT EXISTS fct;
DROP TABLE IF EXISTS fct.records;

CREATE TABLE fct.records(
     device_id                   INT                            NOT NULL
    ,property_id                 INT                            NOT NULL
    ,value                       FLOAT                          NOT NULL
    ,time_stamp                  TIMESTAMP WITH TIME ZONE
    ,batch_date                  TIMESTAMP WITH TIME ZONE

    ,FOREIGN KEY (device_id)    REFERENCES lkp.device       (id)
    ,FOREIGN KEY (property_id)  REFERENCES lkp.property     (id)
);

CREATE TRIGGER logged_actions
AFTER INSERT OR UPDATE OR DELETE ON fct.records
    FOR EACH ROW EXECUTE PROCEDURE audit.if_modified_func();
