/*
	1: Script will generate all columns for the Smart-House database
	2: Script will create appropriate indexes for all columns
*/

-- ALLA SOM HAR CONSTRAINTS SKA HA NONCLUSTERED INDEX



--
--	Create table to represent data that is specific to private users
--	
CREATE TABLE [dbo].[users]
	([User_id] int PRIMARY KEY NOT NULL IDENTITY (1,1),
	[Username] VARCHAR(24) NOT NULL,
	[User_password] VARCHAR(32) NOT NULL,
  [Email] VARCHAR(40) NOT NULL)

GO


--
--	Create table to represent the home-server
--
CREATE TABLE [dbo].[homeserver]
	([Homeserver_id] int PRIMARY KEY NOT NULL IDENTITY(1,1),
	[Server_name] varchar(32) NOT NULL)

GO


--
--  Create table to represent the rooms in a house
--
CREATE TABLE [dbo].[rooms]
  ([Room_id] int PRIMARY KEY NOT NULL IDENTITY (1,1),
  [Room_name] VARCHAR(32) NOT NULL,
  [Homeserver_id] int NOT NULL,

  CONSTRAINT rooms_Homeserver_id_fk FOREIGN KEY (Homeserver_id) REFERENCES [homeserver] ([Homeserver_id]))

  CREATE NONCLUSTERED INDEX rooms_Homeserver_id_idx ON [dbo].[rooms] ([Homeserver_id] ASC);

GO

--
--	Create table to represent data for the devices
--
CREATE TABLE dbo.[devices]
  ([Device_id] INT PRIMARY KEY NOT NULL IDENTITY (1,1),
  [Device_name] VARCHAR(32) NOT NULL,
  [Variable_of_device] VARCHAR(32),
  [Room_id] int NOT NULL,

  CONSTRAINT devices_Room_id_fk FOREIGN KEY (Room_id) REFERENCES [rooms] ([Room_id]))


  CREATE NONCLUSTERED INDEX devices_Room_id_idx ON [dbo].[devices] ([Room_id] ASC);

GO


--
--	Create table to represent different types of sensors
--
CREATE TABLE [dbo].[sensors]
	([Sensor_id] int PRIMARY KEY NOT NULL IDENTITY (1,1),
	[Sensor_type] varchar(32) NOT NULL,
  [Device_id] int NOT NULL,

  CONSTRAINT devices_Device_id_fk FOREIGN KEY (Device_id) REFERENCES [devices] ([Device_id]))

  CREATE NONCLUSTERED INDEX sensors_Devices_id_idx ON [dbo].[sensors] ([Device_id] ASC);

GO


--
--  Many to many relation between users and homeserver
--
CREATE TABLE [dbo].[users_homeserver_maps]
  ([User_id] int NOT NULL,
	[Homeserver_id] int NOT NULL,

  PRIMARY KEY ([User_id], [Homeserver_id]),

  CONSTRAINT users_homeserver_maps_User_id_fk
		FOREIGN KEY ([User_id]) REFERENCES [dbo].[users] ([User_id]),

  CONSTRAINT users_homerserver_maps_Homeserver_id_fk
		FOREIGN KEY ([Homeserver_id]) REFERENCES [dbo].[homeserver] ([Homeserver_id]))

  CREATE NONCLUSTERED INDEX users_homeserver_maps_User_id_idx ON [dbo].[users_homeserver_maps] ([User_id] ASC);
  CREATE NONCLUSTERED INDEX users_homeserver_maps_Homeserver_id_idx ON [dbo].[users_homeserver_maps] ([Homeserver_id] ASC);

GO