create table document_extractions (
    id bigserial primary key not null,
    case_id text not null,
    contents json not null,
    persisted_at timestamp with time zone default(now()),
    updated_at timestamp with time zone default(now()),
    deleted_at timestamp with time zone
);

create index case_id_index on document_extractions(case_id);
