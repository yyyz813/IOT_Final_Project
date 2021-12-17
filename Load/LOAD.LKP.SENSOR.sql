DO
$DO$
BEGIN
IF NOT EXISTS ( ( SELECT * FROM information_schema.tables WHERE table_schema = 'lkp' AND table_name = 'sensor' )) THEN
    RAISE INFO 'Table does not exist';
ELSE

		--======================================================================
		--==   LOAD LKP.SENSOR TABLE TO DEFINE SENSOR ATTRIBUTES
		--======================================================================
		INSERT INTO lkp.sensor
		 (id      ,name             ,description) VALUES
		 (12      ,'SHTC1'          ,'Digital Humidity Sensor')
		,(13      ,'HPMA115C0-002'  ,'PM 2.5 Particle Sensor')
		,(14      ,'DGS-03 968-042' ,'Digital Ozone Sensor')
		,(15      ,'CDM7160-C00'    ,'Carbon Dioxide Sensor')
		,(16      ,'BME680'         ,'Mesures air quality')
		,(17      ,'MICS-6814'      ,'Dectect Pollution ');

END IF;
END;
$DO$
