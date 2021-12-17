--======================================================================
--==    CREATE LKP.DEVICE FOR DEVICE LISTING
--======================================================================
CREATE SCHEMA IF NOT EXISTS lkp;
DROP TABLE IF EXISTS lkp.device;

CREATE TABLE lkp.device
(
     id                 INT                 NOT NULL
    ,name               VARCHAR             NOT NULL
    ,serial_number      VARCHAR             NOT NULL
    ,active_status      INT                 NOT NULL

    ,PRIMARY KEY (id)
);

CREATE TRIGGER logged_actions
AFTER INSERT OR UPDATE OR DELETE ON lkp.device
    FOR EACH ROW EXECUTE PROCEDURE audit.if_modified_func();
