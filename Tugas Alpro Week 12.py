class ShiftManager:
    def __init__(self):
        self.main_shift_queue = []  # Queue untuk karyawan dalam shift kerja utama
        self.backup_shift_stack = [] # Stack untuk karyawan cadangan
    
    # Operasi Queue untuk main_shift_queue
    def add_to_main_shift(self, employee):
        self.main_shift_queue.append(employee)
        print(f"{employee} ditambahkan ke antrian shift kerja utama.")
    
    def start_shift(self):
        if self.main_shift_queue:
            employee = self.main_shift_queue.pop(0)
            print(f"{employee} mulai bekerja dari shift utama.")
            return employee
        else:
            print("Tidak ada karyawan dalam shift kerja utama.")
            return None

    def view_main_shift_queue(self):
        print("Antrian shift kerja utama:", self.main_shift_queue)

    # Operasi Stack untuk backup_shift_stack
    def add_to_backup_shift(self, employee):
        self.backup_shift_stack.append(employee)
        print(f"{employee} ditambahkan ke daftar cadangan shift.")
    
    def use_backup_for_shift(self):
        if self.backup_shift_stack:
            employee = self.backup_shift_stack.pop()
            print(f"{employee} dipanggil dari cadangan untuk bekerja.")
            return employee
        else:
            print("Tidak ada karyawan dalam cadangan shift.")
            return None

    def view_backup_shift_stack(self):
        print("Daftar cadangan shift:", self.backup_shift_stack)


# Program utama untuk mengelola shift kerja
if __name__ == "__main__":
    shift_manager = ShiftManager()
    
    # Menambahkan karyawan ke shift kerja utama (Queue)
    print("Masukkan nama karyawan untuk shift utama (ketik 'stop' untuk berhenti):")
    while True:
        employee = input("Nama karyawan (shift utama): ")
        if employee.lower() == "stop":
            break
        shift_manager.add_to_main_shift(employee)
    
    # Menambahkan karyawan ke shift cadangan (Stack)
    print("\nMasukkan nama karyawan untuk shift cadangan (ketik 'stop' untuk berhenti):")
    while True:
        employee = input("Nama karyawan (shift cadangan): ")
        if employee.lower() == "stop":
            break
        shift_manager.add_to_backup_shift(employee)
    
    # Menampilkan daftar shift kerja utama dan cadangan
    print("\nStatus Shift Kerja Awal:")
    shift_manager.view_main_shift_queue()
    shift_manager.view_backup_shift_stack()
    
    # Memulai shift dari antrian utama
    print("\nMemulai Shift dari Shift Kerja Utama (ketik 'stop' untuk berhenti):")
    while True:
        command = input("Ketik 'start' untuk memulai shift atau 'stop' untuk berhenti: ")
        if command.lower() == "stop":
            break
        elif command.lower() == "start":
            if not shift_manager.start_shift():
                if not shift_manager.use_backup_for_shift():
                    print("Tidak ada karyawan tersedia untuk shift saat ini.")
                    break
    
    # Menampilkan status akhir dari shift kerja utama dan cadangan
    print("\nStatus Shift Kerja Akhir:")
    shift_manager.view_main_shift_queue()
    shift_manager.view_backup_shift_stack()
