CREATE TABLE field_trip (id bigint not null, beginTime timestamp, endTime timestamp, locationId bigint, primary key (id));

CREATE TABLE location (id bigint not null, description varchar(255), latitude bigint, longitude bigint, name varchar(255) not null, primary key (id));

INSERT INTO location (ID, name, latitude, longitude) VALUES (0, 'Whitehall 1', 33.8809715, -83.3518648);
INSERT INTO location (ID, name, latitude, longitude) VALUES (1, 'Whitehall 2', 33.8817197, -83.3460444);
INSERT INTO location (ID, name, latitude, longitude) VALUES (2, 'Scull Shoals 1', 33.7111203, -83.2821948);
INSERT INTO location (ID, name, latitude, longitude) VALUES (3, 'Scull Shoals 2', 33.7179029, -83.2908637);
INSERT into field_trip(ID, locationId, beginTime, endTime) VALUES (0, 1, '2020-10-12 14:00:00', '2020-10-12 16:00:00');
INSERT into field_trip(ID, locationId, beginTime, endTime) VALUES (1, 2, '2020-10-15 14:00:00', '2020-10-12 16:00:00');
INSERT into field_trip(ID, locationId, beginTime, endTime) VALUES (2, 4, '2020-10-21 14:00:00', '2020-10-12 16:00:00');
