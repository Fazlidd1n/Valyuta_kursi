restart_doc:
	docker compose down
	docker rmi -f valyuta_kursi-bot
	docker compose up