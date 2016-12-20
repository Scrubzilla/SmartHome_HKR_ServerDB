-- Stored Procedure for adding a new room.
-- Return 1 is ok
-- Return 0 is fail

CREATE PROCEDURE NewRoom
  @Room_name varchar(32) = null,
  @Homeserver_id int = null

AS

BEGIN
INSERT INTO [dbo].[rooms] (Room_name, Homeserver_id) VALUES (@Room_name, @Homeserver_id);

END