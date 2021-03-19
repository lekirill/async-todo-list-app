CREATE SEQUENCE IF NOT EXISTS public.to_do_list_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;


CREATE TABLE IF NOT EXISTS public.to_do_list (
	id                      bigint NOT NULL DEFAULT nextval('public.to_do_list_seq'),
	short_desc              text NOT NULL,
	description             text NULL,
	is_in_progress          bool NULL,
	is_finished             bool NULL,
	plan_start              timestamp NULL,
	plan_finish             timestamp NULL,
	started_at              timestamp NULL,
	created_at              timestamp NOT NULL DEFAULT now()::timestamp without time zone,
	updated_at              timestamp NULL,
	finished_at             timestamp NULL,

	CONSTRAINT to_do_list_pk PRIMARY KEY (id)

);