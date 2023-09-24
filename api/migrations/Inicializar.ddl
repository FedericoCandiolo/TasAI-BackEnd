-- Plan Free y Premium
INSERT INTO api_plan (id, nombre_plan, precio, tasaciones_maximas, guardados_maximos, activo) VALUES (1, 'Free', 0, 10, 10, true);
INSERT INTO api_plan (id, nombre_plan, precio, tasaciones_maximas, guardados_maximos, activo) VALUES (2, 'Premium', 1000, 200, 200, true);

-- Usuarios admin/admin - Lean/lean123
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, nombre, apellido, apodo, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (1, 'pbkdf2_sha256$720000$L2Xh2J6FORGwDQNqSljZeL$XRVyqIGihYE5+d3MuKJOVCtoYXP8w8OyXXcv9+JzG5A=', null, 1, 'admin', '', '', 1, 1, '2023-09-21 23:27:33.111252', null, null, null, 'admin@admin.com', 1, 0, 0, 2);
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, nombre, apellido, apodo, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (2, 'pbkdf2_sha256$720000$jY2PsY46R7ROZAr0LP9tZq$6+YEfM8mMuew8StqOtVkQpQPx69dCMJQVr9Cjh80Zjw=', null, 0, 'Lean', '', '', 1, 1, '2023-09-21 23:33:14.419687', null, null, null, 'lean@lean.com', 1, 0, 0, 2);
insert into main.api_usuario (id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, nombre, apellido, apodo, email, estado, tasaciones_realizadas, guardados_realizadas, id_plan_id) values (5, 'pbkdf2_sha256$720000$ywOTGBFZ0D80X8JFPXiuuB$GnEbxfUOTqbUkIg/1jA0PIh+Ia85NDgX8AoHQSB/Bik=', null, 0, 'Usuario3', '', '', 0, 1, '2023-09-24 18:27:39.164700', null, null, null, 'Usuario3@Usuario3.com', 1, 0, 0, 1);

-- Propiedades
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (1, 'Balcarce', 2073, 3, 2, 1, 3, 2, 0, 1, 1, 1.1, 1.1, 2);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (2, 'Tapalque', 2741, 3, 1, 1, 2, 1, 0, 0, 0, 1.2, 1.2, 2);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (3, 'Guardia Nacional', 4985, 4, 1, 0, 2, 1, 1, 1, 0, 1.3, 1.3, 2);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (4, 'Rodo', 735, 3, 2, 1, 1, 2, 1, 1, 1, -1.1, -1.1, 2);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (5, 'Tapalque', 234, 2, 1, 1, 2, 2, 0, 1, 0, -1.2, -1.2, 3);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (6, 'Bermejo', 8975, 2, 2, 1, 1, 1, 0, 1, 0, -1.3, -1.3, 3);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (7, 'Mozart', 7852, 2, 2, 1, 1, 2, 0, 0, 0, 2, 2, 3);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (8, 'Chascomus', 5273, 3, 2, 0, 2, 2, 0, 0, 0, 2.2, 2.2, 2);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (9, 'Larrañaga', 2983, 1, 1, 0, 1, 3, 0, 0, 1, -2.2, -2.2, 3);
insert into main.api_propiedad (id, calle, numero, habitaciones, baños, toilets, dormitorios, pisos, pileta, parrilla, jardin, latitud, longitud, id_usuario_id) values (10, 'Bragado', 2419, 4, 2, 1, 3, 1, 1, 0, 1, -3, -3, 3);
