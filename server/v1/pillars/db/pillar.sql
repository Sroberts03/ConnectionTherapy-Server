CREATE TYPE pillar_category AS ENUM ('physical', 'social', 'spiritual', 'intellectual');

CREATE TABLE IF NOT EXISTS pillars (
    id SERIAL PRIMARY KEY,
    name pillar_category NOT NULL,
    color VARCHAR(255) NOT NULL,
    icon_name VARCHAR(255) NOT NULL
);

insert into pillars (name, color, icon_name) values ('physical', '#7afd42ff', 'Dumbbell') ON CONFLICT (name) DO NOTHING;
insert into pillars (name, color, icon_name) values ('social', '#ff8d4bff', 'User') ON CONFLICT (name) DO NOTHING;
insert into pillars (name, color, icon_name) values ('spiritual', '#4d01b6ff', 'Leaf') ON CONFLICT (name) DO NOTHING;
insert into pillars (name, color, icon_name) values ('intellectual', '#0066ffff', 'book') ON CONFLICT (name) DO NOTHING;