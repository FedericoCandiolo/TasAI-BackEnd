-- Plan Free y Premium
INSERT INTO api_plan (id, nombre_plan, precio, tasaciones_maximas, guardados_maximos, activo) VALUES (1, 'Free', 0, 10, 10, true);
INSERT INTO api_plan (id, nombre_plan, precio, tasaciones_maximas, guardados_maximos, activo) VALUES (2, 'Premium', 1000, 200, 200, true);

-- Usuarios admin/admin - Lean/lean123 - Usuario3/Usuario3
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (1, 'pbkdf2_sha256$720000$L2Xh2J6FORGwDQNqSljZeL$XRVyqIGihYE5+d3MuKJOVCtoYXP8w8OyXXcv9+JzG5A=', null, 1, 'admin', '', '', 1, 1, '2023-09-21 23:27:33.111252', 'admin@admin.com', 1, 0, 0, 2);
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (2, 'pbkdf2_sha256$720000$jY2PsY46R7ROZAr0LP9tZq$6+YEfM8mMuew8StqOtVkQpQPx69dCMJQVr9Cjh80Zjw=', null, 0, 'Lean', '', '', 1, 1, '2023-09-21 23:33:14.419687', 'lean@lean.com', 1, 0, 0, 2);
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (5, 'pbkdf2_sha256$720000$ywOTGBFZ0D80X8JFPXiuuB$GnEbxfUOTqbUkIg/1jA0PIh+Ia85NDgX8AoHQSB/Bik=', null, 0, 'Usuario3', '', '', 0, 1, '2023-09-24 18:27:39.164700','Usuario3@Usuario3.com', 1, 0, 0, 1);

-- Propiedades
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (1, 'Balcarce', 2073, 3, 2, 1, 3, 2, 0, 1, 1, 1.1, 1.1, 2, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (2, 'Tapalque', 2741, 3, 1, 1, 2, 1, 0, 0, 0, 1.2, 1.2, 2, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (3, 'Guardia Nacional', 4985, 4, 1, 0, 2, 1, 1, 1, 0, 1.3, 1.3, 2, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (4, 'Rodo', 735, 3, 2, 1, 1, 2, 1, 1, 1, -1.1, -1.1, 2, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (5, 'Tapalque', 234, 2, 1, 1, 2, 2, 0, 1, 0, -1.2, -1.2, 3, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (6, 'Bermejo', 8975, 2, 2, 1, 1, 1, 0, 1, 0, -1.3, -1.3, 3, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (7, 'Mozart', 7852, 2, 2, 1, 1, 2, 0, 0, 0, 2, 2, 3, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (8, 'Chascomus', 5273, 3, 2, 0, 2, 2, 0, 0, 0, 2.2, 2.2, 2, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (9, 'Larrañaga', 2983, 1, 1, 0, 1, 3, 0, 0, 1, -2.2, -2.2, 3, true);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id, esta_guardado) values (10, 'Bragado', 2419, 4, 2, 1, 3, 1, 1, 0, 1, -3, -3, 3, true);

-- Tasaciones
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (1, 300000, 1, 1, 3, '2023-10-03 21:13:17.758174');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (2, 300000, 1, 1, 3, '2023-10-03 21:13:21.426282');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (3, 300000, 1, 1, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (4, 310000, 1, 1, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (5, 310000, 1, 1, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (6, 300000, 1, 2, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (7, 300000, 1, 2, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (8, 300000, 1, 2, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (9, 300000, 1, 2, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (10, 300000, 1, 2, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (11, 100000, 1, 3, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (12, 100000, 1, 3, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (13, 100000, 1, 3, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (14, 100000, 1, 3, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (15, 110000, 1, 3, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (16, 300000, 1, 4, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (17, 300000, 1, 4, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (18, 300000, 1, 4, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (19, 310000, 1, 4, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (20, 300000, 1, 4, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (21, 300000, 1, 5, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (22, 300000, 1, 5, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (23, 300000, 1, 5, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (24, 300000, 1, 5, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (25, 300000, 1, 5, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (26, 300000, 1, 6, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (27, 300000, 1, 6, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (28, 300000, 1, 6, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (29, 300000, 1, 6, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (30, 300000, 1, 6, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (31, 300000, 1, 7, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (32, 300000, 1, 7, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (33, 300000, 1, 7, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (34, 300000, 1, 7, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (35, 300000, 1, 7, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (36, 300000, 1, 8, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (37, 100000, 1, 8, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (38, 100000, 1, 8, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (39, 100000, 1, 8, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (40, 100000, 1, 8, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (41, 110000, 1, 9, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (42, 100000, 1, 9, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (43, 100000, 1, 9, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (44, 100000, 1, 9, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (45, 100000, 1, 9, 3, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (46, 110000, 1, 10, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (47, 100000, 1, 10, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (48, 100000, 1, 10, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (49, 100000, 1, 10, 2, '2023-10-03 21:13:22.737680');
insert into main.api_tasacion (id, precio, esta_guardado, id_propiedad_id, id_usuario_id, fecha_tasacion) values (50, 100000, 1, 10, 2, '2023-10-03 21:13:22.737680');
