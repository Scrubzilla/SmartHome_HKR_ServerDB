CREATE PROCEDURE GetHomeserver
  @User_id INT = NULL

AS

BEGIN

SELECT homeserver.Homeserver_id, Server_name, User_id
FROM homeserver INNER JOIN users_homeserver_maps
    ON homeserver.Homeserver_id = users_homeserver_maps.Homeserver_id
WHERE User_id = @User_id
  END