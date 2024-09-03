import os
import ctypes
import psutil

MALWARE_SIGNATURES = [
    b"\x60\x89\xe5\x31\xc0\x31\xdb\x31\xc9\x31\xd2", # Example shellcode signature
    b"\xeb\xfe",                                     # Infinite loop, common in shellcode
    b"\x90\x90\x90\x90",                              # NOP sled, often used in exploits
    b"\xcc\xcc\xcc\xcc",                              # INT3 instructions, potential breakpoint traps
    b"\x6a\x02\x58\xcd\x80",                          # Syscall payload
]

STACK_CANARY = 0xDEADC0DE
BUFFER_SIZE = 1024

def check_stack_overflow(canary):
    if canary != STACK_CANARY:
        print("Stack overflow detected! Halting execution...")
        exit(1)

def scan_for_malware(memory):
    for i in range(len(memory)):
        for j, signature in enumerate(MALWARE_SIGNATURES):
            sig_len = len(signature)
            if memory[i:i + sig_len] == signature:
                print(f"Malware detected: Signature {j} found at memory offset {i}")
                return True
    return False

def read_memory(pid):
    try:
        with open(f"/proc/{pid}/mem", "rb") as mem_file:
            memory = mem_file.read(BUFFER_SIZE)
            return memory
    except (PermissionError, FileNotFoundError):
        return None

def main():
    stack_canary = STACK_CANARY
    check_stack_overflow(stack_canary)

    for proc in psutil.process_iter(['pid']):
        memory = read_memory(proc.info['pid'])
        if memory and scan_for_malware(memory):
            print(f"Malware detected in process: {proc.info['pid']}")
            break

if __name__ == "__main__":
    main()
