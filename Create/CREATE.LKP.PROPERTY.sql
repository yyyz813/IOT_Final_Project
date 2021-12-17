--======================================================================
--==    CREATE LKP.PROPERTY FOR PROPERTY LISTING
--======================================================================
CREATE SCHEMA IF NOT EXISTS lkp;
DROP TABLE IF EXISTS lkp.property;

CREATE TABLE lkp.property
(
     id             INT             NOT NULL
    ,sensor_id      INT             NOT NULL
    ,name           VARCHAR         NOT NULL
    ,unit           VARCHAR
    ,version        VARCHAR
    ,firmware       VARCHAR

    ,PRIMARY KEY (id)
    ,FOREIGN KEY (sensor_id) REFERENCES lkp.sensor(id)
);

CREATE TRIGGER logged_actions
AFTER INSERT OR UPDATE OR DELETE ON lkp.property
    FOR EACH ROW EXECUTE PROCEDURE audit.if_modified_func();
