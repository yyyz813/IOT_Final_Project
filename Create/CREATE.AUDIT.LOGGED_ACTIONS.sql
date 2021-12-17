--======================================================================
--==	CREATE AUDIT.LOGGED_ACTIONS TABLE FOR LOGGED_ACTIONS
--======================================================================
CREATE SCHEMA IF NOT EXISTS audit;

DROP TABLE IF EXISTS  audit.logged_actions;

CREATE TABLE audit.logged_actions (
    schema_name               TEXT                           NOT NULL
    ,table_name               TEXT                           NOT NULL
    ,user_name                TEXT                           NOT NULL
    ,operation                TEXT                           NOT NULL
    ,change_date              TIMESTAMP WITH TIME ZONE       NOT NULL
    ,previous_data            TEXT                           NULL
    ,new_data                 TEXT                           NULL
);

CREATE OR REPLACE FUNCTION audit.if_modified_func() RETURNS TRIGGER AS $body$
DECLARE
    previousData TEXT;
    newData TEXT;

BEGIN
    IF (TG_OP = 'UPDATE') THEN
        previousData := ROW(OLD.*);
        newData := ROW(NEW.*);
        INSERT INTO audit.logged_actions (schema_name,table_name,user_name,operation,change_date,previous_data,new_data)
        VALUES (TG_TABLE_SCHEMA,TG_TABLE_NAME,current_user,TG_OP,NOW(),previousData,newData);
        RETURN NEW;

    ELSIF (TG_OP = 'DELETE') THEN
        previousData := ROW(OLD.*);
        INSERT INTO audit.logged_actions (schema_name,table_name,user_name,operation,change_date,previous_data)
        VALUES (TG_TABLE_SCHEMA,TG_TABLE_NAME,current_user,TG_OP,NOW(), previousData);
        RETURN OLD;

    ELSIF (TG_OP = 'INSERT') THEN
        newData := ROW(NEW.*);
        INSERT INTO audit.logged_actions (schema_name,table_name,user_name,operation,change_date,new_data)
        VALUES (TG_TABLE_SCHEMA,TG_TABLE_NAME,current_user,TG_OP,NOW(),newData);
        RETURN NEW;

    END IF;
	RETURN NULL;
END;
$body$ LANGUAGE plpgsql;
