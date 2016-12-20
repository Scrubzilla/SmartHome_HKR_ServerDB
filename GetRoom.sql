CREATE PROCEDURE GetRoom
  @Homeserver_id INT = NULL

AS

BEGIN

SELECT Room_name FROM rooms WHERE Homeserver_id = @Homeserver_id

  END