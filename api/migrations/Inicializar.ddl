-- Plan Free y Premium
INSERT INTO api_plan (id, nombre_plan, precio, tasaciones_maximas, guardados_maximos, activo) VALUES (1, 'Free', 0, 10, 10, true);
INSERT INTO api_plan (id, nombre_plan, precio, tasaciones_maximas, guardados_maximos, activo) VALUES (2, 'Premium', 1000, 200, 200, true);
INSERT INTO api_plan (id, nombre_plan, precio, tasaciones_maximas, guardados_maximos, activo) VALUES (3, 'Admin', 9999999999, 9999999999, 9999999999, true);

-- Usuarios admin/admin - Lean/lean123 - Usuario3/Usuario3
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (1, 'pbkdf2_sha256$720000$L2Xh2J6FORGwDQNqSljZeL$XRVyqIGihYE5+d3MuKJOVCtoYXP8w8OyXXcv9+JzG5A=', null, 1, 'admin', '', '', 1, 1, '2023-09-21 23:27:33.111252', 'admin@admin.com', 1, 0, 0, 3);
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (2, 'pbkdf2_sha256$720000$jY2PsY46R7ROZAr0LP9tZq$6+YEfM8mMuew8StqOtVkQpQPx69dCMJQVr9Cjh80Zjw=', null, 0, 'Lean', '', '', 1, 1, '2023-09-21 23:33:14.419687', 'lean@lean.com', 1, 0, 0, 2);
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (5, 'pbkdf2_sha256$720000$ywOTGBFZ0D80X8JFPXiuuB$GnEbxfUOTqbUkIg/1jA0PIh+Ia85NDgX8AoHQSB/Bik=', null, 0, 'Usuario3', '', '', 0, 1, '2023-09-24 18:27:39.164700','Usuario3@Usuario3.com', 1, 0, 0, 1);

-- Propiedades
-- Importar archivo api_propiedad_export.sql

-- Tasaciones
-- Importar archivo api_tasacion_export.sql