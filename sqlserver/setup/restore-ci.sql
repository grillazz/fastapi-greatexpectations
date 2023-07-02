/*

Restore a database from a backup file

*/
CREATE DATABASE AdventureWorksLT2022;
GO

RESTORE DATABASE AdventureWorksLT2022 FROM DISK = 'AdventureWorksLT2022.bak'
    WITH REPLACE,
        MOVE 'AdventureWorksLT2022_Data' TO '/var/opt/mssql/data/AdventureWorksLT2022.mdf',
        MOVE 'AdventureWorksLT2022_log' TO '/var/opt/mssql/data/AdventureWorksLT2022_log.ldf';
GO
