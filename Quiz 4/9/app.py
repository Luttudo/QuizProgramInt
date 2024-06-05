class FlightReservationSystem:
    def __init__(self):
        self.flights = {}  # Dicionário para armazenar voos e suas informações

    def add_flight(self, flight_number, available_seats):
        self.flights[flight_number] = available_seats

    def search_flights(self):
        print("Voos disponíveis:")
        for flight, seats in self.flights.items():
            print(f"Voo {flight}: {seats} assentos disponíveis")

    def reserve_flight(self, flight_number, num_passengers):
        if flight_number in self.flights:
            available_seats = self.flights[flight_number]
            if num_passengers <= available_seats:
                self.flights[flight_number] -= num_passengers
                print(f"Reserva confirmada para {num_passengers} passageiros no voo {flight_number}.")
            else:
                print(f"Não há assentos suficientes no voo {flight_number}.")
        else:
            print(f"Voo {flight_number} não encontrado.")

    def view_reservations(self):
        print("Reservas atuais:")
        for flight, seats in self.flights.items():
            reserved_seats = self.flights[flight] - seats
            print(f"Voo {flight}: {reserved_seats} assentos reservados")

    def cancel_reservation(self, flight_number, num_passengers):
        if flight_number in self.flights:
            self.flights[flight_number] += num_passengers
            print(f"Reserva cancelada para {num_passengers} passageiros no voo {flight_number}.")
        else:
            print(f"Voo {flight_number} não encontrado.")


# Exemplo de uso
if __name__ == "__main__":
    system = FlightReservationSystem()
    system.add_flight("AA123", 100)
    system.add_flight("BB456", 50)

    system.search_flights()
    system.reserve_flight("AA123", 3)
    system.view_reservations()
    system.cancel_reservation("AA123", 1)
    system.view_reservations()
