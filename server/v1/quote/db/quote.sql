create table if not exists quotes (
    id int generated always as identity primary key,
    text text not null,
    author varchar(255) not null,
    approved boolean not null default true,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp on update current_timestamp
);

alter table quotes enable row level security;

insert into quotes (text, author, approved) values
('The greatest gift you can give your children is time — that’s what they remember and treasure the most.', 'Jim Rohn', true);

insert into quotes (text, author, approved) values
('Children learn how to relate to others by observing how their parents relate to them.', 'Melanie Curtin', true);