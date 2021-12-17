
--======================================================================
--==   CREATE LKP.SENSOR TABLE TO DEFINE SENSOR ATTRIBUTES
--======================================================================
CREATE SCHEMA IF NOT EXISTS lkp;
DROP TABLE IF EXISTS lkp.sensor;

CREATE TABLE lkp.sensor(
     id                       INT                    NOT NULL
    ,name                     VARCHAR                NOT NULL
    ,description              VARCHAR

    ,PRIMARY KEY (id)
);

CREATE TRIGGER logged_actions
AFTER INSERT OR UPDATE OR DELETE ON lkp.sensor
    FOR EACH ROW EXECUTE PROCEDURE audit.if_modified_func();
