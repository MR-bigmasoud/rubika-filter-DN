#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import socket

class DNFilterUltimate:
    def __init__(self):
        # Colors and effects for Termux
        self.colors = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'bright_black': '\033[90m',
            'bright_red': '\033[91m',
            'bright_green': '\033[92m',
            'bright_yellow': '\033[93m',
            'bright_blue': '\033[94m',
            'bright_magenta': '\033[95m',
            'bright_cyan': '\033[96m',
            'bright_white': '\033[97m',
            'bold': '\033[1m',
            'dim': '\033[2m',
            'italic': '\033[3m',
            'underline': '\033[4m',
            'blink': '\033[5m',
            'reverse': '\033[7m',
            'hidden': '\033[8m',
            'strike': '\033[9m',
            'reset': '\033[0m'
        }
        
        # Stickers and symbols
        self.stickers = {
            'lock': '🔐',
            'key': '🔑',
            'shield': '🛡️',
            'fire': '🔥',
            'star': '⭐',
            'rocket': '🚀',
            'warning': '⚠️',
            'check': '✅',
            'cross': '❌',
            'gear': '⚙️',
            'link': '🔗',
            'file': '📁',
            'server': '🖥️',
            'code': '💻',
            'terminal': '⌨️',
            'signal': '📡',
            'satellite': '🛰️',
            'alien': '👽',
            'robot': '🤖',
            'dragon': '🐉',
            'skull': '💀',
            'ghost': '👻',
            'zap': '⚡',
            'boom': '💥',
            'sparkles': '✨',
            'globe': '🌐',
            'cloud': '☁️',
            'cyclone': '🌀',
            'tornado': '🌪️',
            'volcano': '🌋',
            'comet': '☄️',
            'atom': '⚛️',
            'biohazard': '☣️',
            'radioactive': '☢️',
            'medical': '⚕️',
            'scales': '⚖️',
            'hammer': '⚒️',
            'pick': '⛏️',
            'sword': '⚔️',
            'gun': '🔫',
            'bomb': '💣',
            'dagger': '🗡️',
            'shield2': '🛡',
            'helmet': '⛑️',
            'crown': '👑',
            'trophy': '🏆',
            'medal': '🏅',
            'flag': '🏴',
            'book': '📚',
            'pencil': '✏️',
            'bulb': '💡',
            'magnifier': '🔍',
            'chart': '📊',
            'info': 'ℹ️',
            'teacher': '🧑‍🏫'
        }
        
        # Codes database
        self.codes = {
            # Account codes
            'account': "6.5.1.8/f/h u//5.7.3.1.9.6.6.0.3.9.4.3.8.4.1.4.7.8.2.9.5.6.7.2.8.6.5.3.1.1.5.6.1.7.1.6,3/",
            'channel': "(7.8.9.2.d/f///y//6065///g.k.4.6.7.8.2.3.5.6.7.3.2.9.3.9.1.5.3.6.2.9.6/)",
            
            # For verification in total mix
            'account_code': "@Hack.rubik.filter.DN",
            'mixer_code': "@Hack.rubik.filter.DN",
            'github_code': "https://github.com/(6.5.1.8/f/h u//.7.3.1.9.6.6.0.3.9.4.3.8.4.1.4.7.8.2.9.5.6.7.2.8.6.5.3.1.1.5.6.1.7.1.6,3/)",
            'channel_code1': "(7.8.9.2.d/f///y//6065///g.k.4.6.7.8.2.3.5.6.7.3.2.9.3.9.1.5.3.6.2.9.6/)",
            
            # Mixed codes results
            'mixed_account': """https://github.com/arthur0010/cod2.8.8.9/f/h.u//6.2.22.6.5.0.6.4.8.7.7.8.6.5.9.9.5.2.5.7.3.5.4.9.3.3.2.4.9.3.9.7.2.9.6.4/-filtering-keristoferhttps://github.com/arthur0010/cod-6.4.2.7/e////f.h/1.7.3.0.1.2.6.6.2.4.6.0.9.7.4.3.1.8.7.6.1.3.9.3.4.8.3.5.8.5.9.0.1.2.1.4.0/filtering-keristoferhttps://github.com/arthur0010/cod-5.4.2.9/f//d/3.0.1.8.0.9.8.8.5.4.9.5.2.8.4.4.7.6.9.6.9.1.3.7.7.9.1.8.8.0.3.3.8.8.0.4.2/filtering-keristofercom/arthur0010/cod-(6.5.1.8/f/hu//5.7.3.1.9.6.6.0.3.9.4.3.8.4.1.4.7.8.2.9.5.6.7.2.8.6.5.3.1.1.5.6.1.7.1.6,3/)filtering@Tahaee1395.106.8.15@:)GORDYiteratobikaral+/Filterobika>(6.82.37f/h.g//0.4.6.0.6.89.11.9.0.4.0.5.4.8.5.3.7.4.8.0.5.3.1.8.3.0.8.9.3.4.1.1.8.9.7/)""",
            
            'mixed_channel': """https://github.com/arthur0010/cod2.8.8.9/f/h.u//6.2.22.6.5.0.6.4.8.7.7.8.6.5.9.9.5.2.5.7.3.5.4.9.3.3.2.4.9.3.9.7.2.9.6.4/-filtering-keristoferhttps://github.com/arthur0010/cod-6.4.2.7/e////f.h/1.7.3.0.1.2.6.6.2.4.6.0.9.7.4.3.1.8.7.6.1.3.9.3.4.8.3.5.8.5.9.0.1.2.1.4.0/filtering-keristoferhttps://github.com/arthur0010/cod-5.4.2.9/f//d/3.0.1.8.0.9.8.8.5.4.9.5.2.8.4.4.7.6.9.6.9.1.3.7.7.9.1.8.8.0.3.3.8.8.0.4.2/filtering-keristofercom/arthur0010/cod-(6.5.1.8/f/hu//5.7.3.1.9.6.6.0.3.9.4.3.8.4.1.4.7.8.2.9.5.6.7.2.8.6.5.3.1.1.5.6.1.7.1.6,3/)filtering@Tahaee1395.106.8.15@:)GORDYiteratobikaral+/Filterobika>(/5.6.7.filtering_rubika///6.5.3.8.h//310.561///5.1.1.6)"""
        }
        
        self.running = True

    def check_internet(self, timeout=3):
        """Check internet connection"""
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except socket.error:
            return False

    def show_no_internet_message(self):
        """Show no internet connection message with effects"""
        self.clear()
        
        print(f"\n{self.colors['bright_red']}{self.stickers['warning']}{'⚠'*58}{self.stickers['warning']}{self.colors['reset']}")
        
        # Blinking effect for the message
        for _ in range(3):
            print(f"{self.colors['blink']}{self.colors['bold']}{self.colors['bright_red']}")
            print(f"{self.stickers['cross']} NO INTERNET CONNECTION {self.stickers['cross']}")
            print(f"{self.colors['reset']}")
            time.sleep(0.5)
            
            self.clear()
            print(f"\n{self.colors['bright_red']}{self.stickers['warning']}{'⚠'*58}{self.stickers['warning']}{self.colors['reset']}")
            
            print(f"{self.colors['bold']}{self.colors['bright_yellow']}")
            print(f"{self.stickers['signal']} PLEASE CHECK YOUR CONNECTION {self.stickers['signal']}")
            print(f"{self.colors['reset']}")
            time.sleep(0.5)
        
        # Final static message
        self.clear()
        print(f"\n{self.colors['bright_red']}{self.stickers['warning']}{'═'*58}{self.stickers['warning']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}")
        print(f"{self.stickers['cross']} CONNECTION ERROR {self.stickers['cross']}")
        print(f"{self.colors['reset']}")
        print(f"{self.colors['bright_red']}{self.stickers['warning']}{'═'*58}{self.stickers['warning']}{self.colors['reset']}\n")
        
        print(f"{self.colors['bright_yellow']}{self.stickers['signal']} PLEASE CHECK YOUR INTERNET CONNECTION {self.stickers['signal']}{self.colors['reset']}")
        print(f"{self.colors['bright_cyan']}{self.stickers['globe']} AND TRY AGAIN {self.stickers['globe']}{self.colors['reset']}\n")
        
        print(f"{self.colors['bright_red']}{self.stickers['warning']}{'═'*58}{self.stickers['warning']}{self.colors['reset']}")
        
        # Wait and exit
        time.sleep(3)
        sys.exit(1)

    def clear(self):
        os.system('clear')

    def print_effect(self, text, effect='typing', delay=0.03, color='white'):
        """Print text with special effects"""
        colors_list = list(self.colors.keys())[:16]  # Exclude effects
        
        if effect == 'typing':
            for char in text:
                print(f"{self.colors.get(color, self.colors['white'])}{char}{self.colors['reset']}", end='', flush=True)
                time.sleep(delay)
            print()
        
        elif effect == 'rainbow':
            for i, char in enumerate(text):
                color = colors_list[i % len(colors_list)]
                print(f"{self.colors[color]}{char}{self.colors['reset']}", end='', flush=True)
                time.sleep(delay)
            print()
        
        elif effect == 'matrix':
            matrix_chars = "01█▓▒░"
            for char in text:
                if random.random() < 0.3:
                    print(f"{self.colors['bright_green']}{random.choice(matrix_chars)}{self.colors['reset']}", end='', flush=True)
                    print(f"\b{self.colors['green']}{char}{self.colors['reset']}", end='', flush=True)
                else:
                    print(f"{self.colors['green']}{char}{self.colors['reset']}", end='', flush=True)
                time.sleep(delay * 0.5)
            print()
        
        elif effect == 'glitch':
            glitch_chars = "!@#$%&*"
            for char in text:
                if random.random() < 0.2:
                    print(f"{self.colors['bright_red']}{random.choice(glitch_chars)}{self.colors['reset']}", end='', flush=True)
                    time.sleep(0.05)
                    print(f"\b{self.colors['bright_blue']}{char}{self.colors['reset']}", end='', flush=True)
                else:
                    print(f"{self.colors['bright_blue']}{char}{self.colors['reset']}", end='', flush=True)
                time.sleep(delay)
            print()

    def loading_animation(self):
        """Ultimate loading animation with stickers"""
        self.clear()
        
        # First check internet connection
        print(f"\n{self.colors['bright_cyan']}{self.colors['blink']}Checking internet connection...{self.colors['reset']}")
        time.sleep(1)
        
        if not self.check_internet():
            self.show_no_internet_message()
        
        # Hacking intro animation
        print(f"\n{self.colors['bright_green']}{self.colors['blink']}╔{'═'*58}╗{self.colors['reset']}")
        print(f"{self.colors['bright_green']}║{self.colors['reset']}{self.colors['bold']}{self.colors['bright_white']}     INITIALIZING DN FILTER SYSTEM...      {self.colors['reset']}{self.colors['bright_green']}║{self.colors['reset']}")
        print(f"{self.colors['bright_green']}╚{'═'*58}╝{self.colors['reset']}\n")
        
        loading_sequence = [
            (f"{self.stickers['alien']}  !!", 0.1),
            (f"{self.stickers['signal']}  lod....", 0.15),
            (f"{self.stickers['terminal']}  n/y", 0.1),
            (f"{self.colors['dim']}....", 0.08),
            (f"{self.colors['dim']}......", 0.08),
            (f"{self.colors['dim']}.........", 0.08),
            (f"{self.colors['dim']}..................", 0.08),
            (f"{self.colors['dim']}.........................", 0.08),
            (f"{self.colors['dim']}.............................", 0.08),
            (f"{self.colors['dim']}...............................", 0.08),
            (f"{self.colors['dim']}.................................", 0.08),
            (f"{self.colors['dim']}....................................", 0.08),
            (f"{self.stickers['cloud']}  ~iegn", 0.2),
            (f"{self.stickers['server']}  cood info server", 0.25),
            (f"{self.stickers['code']}  script server cood", 0.25),
            (f"{self.stickers['satellite']}  server1:y//d/f", 0.2),
            (f"{self.stickers['satellite']}  server2:f//d/", 0.2),
            (f"{self.stickers['satellite']}  server3:g/d//", 0.2),
            (f"{self.stickers['satellite']}  server4:d//f/h", 0.2),
            (f"{self.stickers['satellite']}  server5:f//a/y", 0.2),
            (f"{self.stickers['robot']}  making script maxtor", 0.3),
            (f"{self.stickers['gear']}  script making cood filter rubika.apk 2.9.5 80%", 0.4),
            (f"{self.stickers['server']}  script server", 0.25),
            (f"{self.stickers['globe']}  script connect server rubika.ir/rubika.com/ file os server", 0.35),
            (f"{self.stickers['shield']}  cood filter group 90% apn cood proxy-server", 0.3),
            (f"{self.stickers['lock']}  cood filter account rubika 87% apn cood filter proxy-port:8000", 0.3),
            (f"{self.stickers['link']}  cood filter chaneel rubika 78% apn proxy file port:auth", 0.3),
        ]
        
        for text, delay in loading_sequence:
            self.print_effect(text, effect='matrix' if random.random() > 0.7 else 'typing', 
                            delay=delay*0.5, color='bright_green')
            time.sleep(delay)
        
        # Final loading bar
        print(f"\n{self.colors['bright_cyan']}[{self.colors['reset']}", end='')
        for i in range(40):
            print(f"{self.colors['bright_green']}█{self.colors['reset']}", end='', flush=True)
            time.sleep(0.05)
            if i == 10:
                print(f"{self.colors['bright_yellow']} LOADING {self.colors['reset']}", end='')
            elif i == 20:
                print(f"{self.colors['bright_blue']} ENCRYPTING {self.colors['reset']}", end='')
            elif i == 30:
                print(f"{self.colors['bright_magenta']} FINALIZING {self.colors['reset']}", end='')
        print(f"{self.colors['bright_cyan']}]{self.colors['reset']}")
        
        # Success message with animation
        time.sleep(0.5)
        print(f"\n{self.colors['bright_green']}{self.stickers['check']} SYSTEM READY! {self.stickers['rocket']}")
        print(f"{self.colors['bright_cyan']}{self.stickers['zap']} DN FILTER ACTIVATED {self.stickers['zap']}{self.colors['reset']}")
        time.sleep(1.5)

    def show_banner(self):
        """Show animated DN banner with stickers"""
        self.clear()
        
        banner = f"""
{self.colors['bright_red']}{self.colors['blink']}{self.stickers['fire']}{'═'*52}{self.stickers['fire']}{self.colors['reset']}
{self.colors['bright_red']}{self.colors['bold']}
{self.stickers['dragon']}   ██████╗ ███╗   ██╗     ██████╗ ██╗███████╗██████╗   {self.stickers['dragon']}
{self.stickers['skull']}   ██╔══██╗████╗  ██║    ██╔═══██╗██║██╔════╝██╔══██╗  {self.stickers['skull']}
{self.stickers['ghost']}   ██║  ██║██╔██╗ ██║    ██║   ██║██║█████╗  ██████╔╝  {self.stickers['ghost']}
{self.stickers['alien']}   ██║  ██║██║╚██╗██║    ██║   ██║██║██╔══╝  ██╔══██╗  {self.stickers['alien']}
{self.stickers['robot']}   ██████╔╝██║ ╚████║    ╚██████╔╝██║███████╗██║  ██║  {self.stickers['robot']}
{self.stickers['boom']}   ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝  {self.stickers['boom']}
{self.colors['reset']}
{self.colors['bright_cyan']}{self.colors['bold']}
{self.stickers['crown']}   ╔═══════════════════════════════════════════════╗   {self.stickers['crown']}
{self.stickers['trophy']}   ║        {self.stickers['zap']} DN FILTER TERMINAL v2.0 {self.stickers['zap']}        ║   {self.stickers['trophy']}
{self.stickers['medal']}   ╚═══════════════════════════════════════════════╝   {self.stickers['medal']}
{self.colors['reset']}
{self.colors['bright_red']}{self.colors['blink']}{self.stickers['fire']}{'═'*52}{self.stickers['fire']}{self.colors['reset']}
"""
        
        # Animate banner line by line
        for line in banner.split('\n'):
            self.print_effect(line, effect='typing', delay=0.01, color='white')
            time.sleep(0.03)
        
        time.sleep(0.5)

    def main_menu(self):
        """Interactive main menu with stickers"""
        menu = f"""
{self.colors['bright_cyan']}{self.stickers['cyclone']}{'━'*58}{self.stickers['cyclone']}{self.colors['reset']}
{self.colors['bold']}{self.colors['bright_white']}        {self.stickers['star']} MAIN CONTROL PANEL {self.stickers['star']}{self.colors['reset']}
{self.colors['bright_cyan']}{self.stickers['cyclone']}{'━'*58}{self.stickers['cyclone']}{self.colors['reset']}

{self.colors['bright_green']}{self.stickers['key']}  [1] {self.colors['reset']}{self.colors['cyan']}FILTER CODES{self.colors['reset']}
{self.colors['bright_yellow']}{self.stickers['link']}  [2] {self.colors['reset']}{self.colors['cyan']}ACCOUNT CODE{self.colors['reset']}
{self.colors['bright_magenta']}{self.stickers['gear']}  [3] {self.colors['reset']}{self.colors['cyan']}MIXER CODE{self.colors['reset']}
{self.colors['bright_blue']}{self.stickers['volcano']}  [4] {self.colors['reset']}{self.colors['cyan']}TOTAL MIX{self.colors['reset']}
{self.colors['bright_cyan']}{self.stickers['globe']}  [5] {self.colors['reset']}{self.colors['cyan']}GITHUB CODE FILTER{self.colors['reset']}
{self.colors['bright_green']}{self.stickers['book']}  [6] {self.colors['reset']}{self.colors['cyan']}HOW TO USE{self.colors['reset']}
{self.colors['bright_red']}{self.stickers['skull']}  [7] {self.colors['reset']}{self.colors['cyan']}EXIT SYSTEM{self.colors['reset']}

{self.colors['bright_cyan']}{self.stickers['cyclone']}{'━'*58}{self.stickers['cyclone']}{self.colors['reset']}
"""
        
        # Print menu with effect
        for line in menu.split('\n'):
            print(line)
            time.sleep(0.02)
        
        while True:
            choice = input(f"\n{self.colors['blink']}{self.colors['bright_yellow']}{self.stickers['warning']}  SELECT [{self.stickers['zap']}1-7{self.stickers['zap']}]: {self.colors['reset']}").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return choice
            else:
                print(f"{self.colors['bright_red']}{self.stickers['cross']} INVALID! {self.stickers['cross']}{self.colors['reset']}")

    def show_how_to_use(self):
        """Display how to use instructions with epic effects"""
        self.clear()
        
        # Header with effects
        print(f"\n{self.colors['bright_green']}{self.stickers['book']}{'━'*58}{self.stickers['book']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}     {self.stickers['teacher']} HOW TO USE DN FILTER {self.stickers['teacher']}{self.colors['reset']}")
        print(f"{self.colors['bright_green']}{self.stickers['book']}{'━'*58}{self.stickers['book']}{self.colors['reset']}\n")
        
        # Loading animation
        print(f"{self.colors['bright_yellow']}{self.stickers['rocket']} LOADING TUTORIAL", end='')
        for _ in range(3):
            print(f"{self.colors['blink']}.{self.colors['reset']}", end='', flush=True)
            time.sleep(0.3)
        print(f"{self.colors['reset']}\n")
        
        # Instructions with step-by-step animation
        instructions = [
            f"{self.colors['bold']}{self.colors['bright_yellow']}{self.stickers['warning']} STEP 1: {self.colors['reset']}{self.colors['cyan']}برای استفاده اول هر 3 کد را در مخلوط کان بزارید",
            f"{self.colors['bold']}{self.colors['bright_green']}{self.stickers['check']} STEP 2: {self.colors['reset']}{self.colors['cyan']}کد اصلی را کپی کنید",
            f"{self.colors['bold']}{self.colors['bright_blue']}{self.stickers['zap']} STEP 3: {self.colors['reset']}{self.colors['cyan']}۵ بار در گزارش سایر موارد بزنید",
            f"{self.colors['bold']}{self.colors['bright_magenta']}{self.stickers['fire']} STEP 4: {self.colors['reset']}{self.colors['cyan']}و ۱۵ بار مستحجن بزنید",
            f"",
            f"{self.colors['bright_red']}{self.stickers['flag']} کانال روبیکا: {self.colors['reset']}{self.colors['bright_cyan']}@DN-hackers",
            f"{self.colors['bright_yellow']}{self.stickers['crown']} توسط: {self.colors['reset']}{self.colors['bright_green']}Bigmasoud and hichkas"
        ]
        
        # Display each instruction with effect
        for i, instruction in enumerate(instructions):
            if i < 4:  # For steps
                self.print_effect(instruction, effect='typing', delay=0.03, color='white')
                time.sleep(0.5)
                
                # Show step icon animation
                step_icons = [self.stickers['bulb'], self.stickers['magnifier'], self.stickers['chart'], self.stickers['info']]
                print(f"    {self.colors['bright_cyan']}{step_icons[i]}{'─'*50}{step_icons[i]}{self.colors['reset']}\n")
                time.sleep(0.3)
            else:
                # For other lines
                self.print_effect(instruction, effect='rainbow', delay=0.02)
                time.sleep(0.5)
        
        # Visual demonstration
        print(f"\n{self.colors['bright_green']}{self.stickers['zap']}{'━'*58}{self.stickers['zap']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}{self.stickers['pencil']} VISUAL DEMONSTRATION:{self.colors['reset']}\n")
        
        demo_steps = [
            f"{self.colors['dim']}1. Rubika App → {self.colors['bright_green']}Reports{self.colors['dim']} → {self.colors['bright_yellow']}Other{self.colors['reset']}",
            f"{self.colors['dim']}2. {self.colors['bright_cyan']}Paste Code 5 times{self.colors['reset']}",
            f"{self.colors['dim']}3. {self.colors['bright_magenta']}Click Mostahjen 15 times{self.colors['reset']}",
            f"{self.colors['dim']}4. {self.colors['bright_green']}Wait for activation{self.colors['reset']}",
            f"{self.colors['dim']}5. {self.colors['bright_yellow']}Filter will be applied!{self.colors['reset']}"
        ]
        
        for step in demo_steps:
            self.print_effect(f"   {self.stickers['check']} {step}", effect='typing', delay=0.02, color='bright_white')
            time.sleep(0.3)
        
        # Important notes
        print(f"\n{self.colors['bright_red']}{self.stickers['warning']}{'⚠'*58}{self.stickers['warning']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_yellow']}{self.stickers['info']} IMPORTANT NOTES:{self.colors['reset']}\n")
        
        notes = [
            f"{self.colors['bright_cyan']}• {self.stickers['lock']} Ensure you have latest Rubika version",
            f"{self.colors['bright_magenta']}• {self.stickers['shield']} Use codes within 24 hours of generation",
            f"{self.colors['bright_green']}• {self.stickers['key']} Codes are single-use only",
            f"{self.colors['bright_yellow']}• {self.stickers['globe']} Internet connection required",
            f"{self.colors['bright_red']}• {self.stickers['skull']} Use responsibly!"
        ]
        
        for note in notes:
            self.print_effect(f"   {note}", effect='typing', delay=0.02, color='white')
            time.sleep(0.2)
        
        print(f"\n{self.colors['bright_green']}{self.stickers['book']}{'━'*58}{self.stickers['book']}{self.colors['reset']}")
        
        # Wait for user
        input(f"\n{self.colors['blink']}{self.colors['bright_yellow']}{self.stickers['rocket']}  PRESS ENTER TO RETURN... {self.colors['reset']}")

    def filter_codes_menu(self):
        """Filter codes submenu"""
        self.clear()
        
        menu = f"""
{self.colors['bright_blue']}{self.stickers['shield']}{'─'*58}{self.stickers['shield']}{self.colors['reset']}
{self.colors['bold']}{self.colors['bright_white']}        {self.stickers['lock']} FILTER CODE VAULT {self.stickers['lock']}{self.colors['reset']}
{self.colors['bright_blue']}{self.stickers['shield']}{'─'*58}{self.stickers['shield']}{self.colors['reset']}

{self.colors['bright_green']}{self.stickers['key']}  [1] {self.colors['reset']}{self.colors['cyan']}ACCOUNT FILTER CODE{self.colors['reset']}
{self.colors['bright_yellow']}{self.stickers['satellite']}  [2] {self.colors['reset']}{self.colors['cyan']}CHANNEL FILTER CODE{self.colors['reset']}
{self.colors['bright_red']}{self.stickers['ghost']}  [3] {self.colors['reset']}{self.colors['cyan']}BACK TO MAIN{self.colors['reset']}

{self.colors['bright_blue']}{self.stickers['shield']}{'─'*58}{self.stickers['shield']}{self.colors['reset']}
"""
        
        for line in menu.split('\n'):
            print(line)
            time.sleep(0.02)
        
        while True:
            choice = input(f"\n{self.colors['blink']}{self.colors['bright_yellow']}{self.stickers['warning']}  CHOOSE [{self.stickers['zap']}1-3{self.stickers['zap']}]: {self.colors['reset']}").strip()
            
            if choice == '1':
                self.show_code("ACCOUNT FILTER CODE", self.codes['account'], 'account')
                break
            elif choice == '2':
                self.show_code("CHANNEL FILTER CODE", self.codes['channel'], 'channel')
                break
            elif choice == '3':
                break
            else:
                print(f"{self.colors['bright_red']}{self.stickers['cross']} INVALID SELECTION! {self.stickers['cross']}{self.colors['reset']}")

    def show_code(self, title, code, code_type='normal'):
        """Show code with epic effects"""
        self.clear()
        
        # Header with effects
        print(f"\n{self.colors['bright_green']}{self.stickers['zap']}{'━'*58}{self.stickers['zap']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}     {self.stickers['file']} {title} {self.stickers['file']}{self.colors['reset']}")
        print(f"{self.colors['bright_green']}{self.stickers['zap']}{'━'*58}{self.stickers['zap']}{self.colors['reset']}\n")
        
        # Loading animation
        print(f"{self.colors['bright_yellow']}{self.stickers['rocket']} DECRYPTING", end='')
        for _ in range(3):
            print(f"{self.colors['blink']}.{self.colors['reset']}", end='', flush=True)
            time.sleep(0.4)
        print(f"{self.colors['reset']}\n")
        
        # Display code with special effect
        if code_type == 'mixed':
            effect = 'matrix'
        elif code_type in ['account', 'channel']:
            effect = 'glitch'
        else:
            effect = 'rainbow'
        
        self.print_effect(f"{self.colors['bright_cyan']}{code}{self.colors['reset']}", 
                         effect=effect, delay=0.001 if len(code) > 100 else 0.02)
        
        # Footer with instructions for mixed codes
        print(f"\n{self.colors['bright_green']}{self.stickers['zap']}{'━'*58}{self.stickers['zap']}{self.colors['reset']}")
        
        if 'MIX' in title or 'mixed' in code_type:
            print(f"\n{self.colors['bright_red']}{self.stickers['warning']} CRITICAL INSTRUCTIONS:{self.colors['reset']}")
            print(f"{self.colors['bright_yellow']}{self.stickers['key']} 1. Copy this code 5 times{self.colors['reset']}")
            print(f"{self.colors['bright_cyan']}{self.stickers['globe']} 2. In Rubika: Reports > Other{self.colors['reset']}")
            print(f"{self.colors['bright_magenta']}{self.stickers['fire']} 3. Paste Mostahjen 15 times{self.colors['reset']}")
            print(f"{self.colors['bright_green']}{self.stickers['check']} 4. Wait for magic to happen!{self.colors['reset']}")
            print(f"{self.colors['bright_green']}{self.stickers['zap']}{'━'*58}{self.stickers['zap']}{self.colors['reset']}")
        
        input(f"\n{self.colors['blink']}{self.colors['bright_yellow']}{self.stickers['rocket']}  PRESS ENTER TO CONTINUE... {self.colors['reset']}")

    def show_account_code(self):
        self.show_code("ACCOUNT CODE", self.codes['account_code'], 'account')

    def show_mixer_code(self):
        self.show_code("MIXER CODE", self.codes['mixer_code'], 'mixer')

    def show_github_code_filter(self):
        self.show_code("GITHUB CODE FILTER", self.codes['github_code'], 'github')

    def total_mix_menu(self):
        """Total mix selection menu"""
        self.clear()
        
        menu = f"""
{self.colors['bright_magenta']}{self.stickers['volcano']}{'─'*58}{self.stickers['volcano']}{self.colors['reset']}
{self.colors['bold']}{self.colors['bright_white']}        {self.stickers['atom']} TOTAL MIX FUSION {self.stickers['atom']}{self.colors['reset']}
{self.colors['bright_magenta']}{self.stickers['volcano']}{'─'*58}{self.stickers['volcano']}{self.colors['reset']}

{self.colors['bright_green']}{self.stickers['biohazard']}  [1] {self.colors['reset']}{self.colors['cyan']}ACCOUNT MIX FUSION{self.colors['reset']}
{self.colors['bright_red']}{self.stickers['radioactive']}  [2] {self.colors['reset']}{self.colors['cyan']}CHANNEL MIX FUSION{self.colors['reset']}
{self.colors['bright_yellow']}{self.stickers['ghost']}  [3] {self.colors['reset']}{self.colors['cyan']}BACK TO MAIN{self.colors['reset']}

{self.colors['bright_magenta']}{self.stickers['volcano']}{'─'*58}{self.stickers['volcano']}{self.colors['reset']}
"""
        
        for line in menu.split('\n'):
            print(line)
            time.sleep(0.02)
        
        while True:
            choice = input(f"\n{self.colors['blink']}{self.colors['bright_yellow']}{self.stickers['warning']}  SELECT FUSION [{self.stickers['zap']}1-3{self.stickers['zap']}]: {self.colors['reset']}").strip()
            
            if choice == '1':
                self.verify_account_mix()
                break
            elif choice == '2':
                self.verify_channel_mix()
                break
            elif choice == '3':
                break
            else:
                print(f"{self.colors['bright_red']}{self.stickers['cross']} INVALID FUSION! {self.stickers['cross']}{self.colors['reset']}")

    def verify_account_mix(self):
        """Verify account mix with epic effects"""
        self.clear()
        
        print(f"\n{self.colors['bright_yellow']}{self.stickers['warning']}{'⚠'*58}{self.stickers['warning']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}     {self.stickers['biohazard']} ACCOUNT MIX VERIFICATION {self.stickers['biohazard']}{self.colors['reset']}")
        print(f"{self.colors['bright_yellow']}{self.stickers['warning']}{'⚠'*58}{self.stickers['warning']}{self.colors['reset']}\n")
        
        required_codes = [
            (f"{self.stickers['lock']} Account Filter Code", self.codes['account']),
            (f"{self.stickers['key']} Account Code", self.codes['account_code']),
            (f"{self.stickers['globe']} Github Code", self.codes['github_code'])
        ]
        
        user_codes = []
        
        for i, (name, correct_code) in enumerate(required_codes, 1):
            print(f"\n{self.colors['bright_cyan']}{self.stickers['zap']} [{i}] Enter {name}:{self.colors['reset']}")
            user_code = input(f"{self.colors['blink']}{self.colors['bright_yellow']}{self.stickers['terminal']} > {self.colors['reset']}").strip()
            user_codes.append(user_code)
            
            if user_code == correct_code:
                print(f"{self.colors['bright_green']}{self.stickers['check']} VERIFIED! {self.stickers['check']}{self.colors['reset']}")
            else:
                print(f"{self.colors['bright_red']}{self.stickers['cross']} REJECTED! {self.stickers['cross']}{self.colors['reset']}")
            
            time.sleep(0.5)
        
        # Epic verification sequence
        print(f"\n{self.colors['bright_cyan']}{self.stickers['cyclone']}{'─'*58}{self.stickers['cyclone']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}{self.stickers['atom']} INITIATING FUSION SEQUENCE...{self.colors['reset']}")
        
        for _ in range(5):
            print(f"{self.colors['blink']}{random.choice(['█', '▓', '▒', '░'])}", end='', flush=True)
            time.sleep(0.2)
        
        all_correct = all(user_codes[i] == required_codes[i][1] for i in range(3))
        
        if all_correct:
            print(f"\n\n{self.colors['bright_green']}{self.colors['blink']}{self.stickers['check']} FUSION SUCCESSFUL! {self.stickers['check']}{self.colors['reset']}")
            time.sleep(1)
            self.show_code("ACCOUNT MIX CODE", self.codes['mixed_account'], 'mixed')
        else:
            print(f"\n\n{self.colors['bright_red']}{self.colors['blink']}{self.stickers['cross']} FUSION FAILED! {self.stickers['cross']}{self.colors['reset']}")
            print(f"{self.colors['bright_yellow']}{self.stickers['warning']} RE-ENTER CORRECT CODES!{self.colors['reset']}")
            time.sleep(2)
            self.verify_account_mix()

    def verify_channel_mix(self):
        """Verify channel mix with epic effects"""
        self.clear()
        
        print(f"\n{self.colors['bright_yellow']}{self.stickers['warning']}{'⚠'*58}{self.stickers['warning']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}     {self.stickers['radioactive']} CHANNEL MIX VERIFICATION {self.stickers['radioactive']}{self.colors['reset']}")
        print(f"{self.colors['bright_yellow']}{self.stickers['warning']}{'⚠'*58}{self.stickers['warning']}{self.colors['reset']}\n")
        
        required_codes = [
            (f"{self.stickers['satellite']} Channel Filter Code", self.codes['channel_code1']),
            (f"{self.stickers['key']} Account Code", self.codes['account_code']),
            (f"{self.stickers['globe']} Github Code", self.codes['github_code'])
        ]
        
        user_codes = []
        
        for i, (name, correct_code) in enumerate(required_codes, 1):
            print(f"\n{self.colors['bright_cyan']}{self.stickers['zap']} [{i}] Enter {name}:{self.colors['reset']}")
            user_code = input(f"{self.colors['blink']}{self.colors['bright_yellow']}{self.stickers['terminal']} > {self.colors['reset']}").strip()
            user_codes.append(user_code)
            
            if user_code == correct_code:
                print(f"{self.colors['bright_green']}{self.stickers['check']} VERIFIED! {self.stickers['check']}{self.colors['reset']}")
            else:
                print(f"{self.colors['bright_red']}{self.stickers['cross']} REJECTED! {self.stickers['cross']}{self.colors['reset']}")
            
            time.sleep(0.5)
        
        # Epic verification sequence
        print(f"\n{self.colors['bright_cyan']}{self.stickers['cyclone']}{'─'*58}{self.stickers['cyclone']}{self.colors['reset']}")
        print(f"{self.colors['bold']}{self.colors['bright_white']}{self.stickers['comet']} INITIATING CHANNEL FUSION...{self.colors['reset']}")
        
        for _ in range(5):
            print(f"{self.colors['blink']}{random.choice(['⚡', '💥', '✨', '🌀'])}", end='', flush=True)
            time.sleep(0.2)
        
        all_correct = all(user_codes[i] == required_codes[i][1] for i in range(3))
        
        if all_correct:
            print(f"\n\n{self.colors['bright_green']}{self.colors['blink']}{self.stickers['check']} CHANNEL FUSION COMPLETE! {self.stickers['check']}{self.colors['reset']}")
            time.sleep(1)
            self.show_code("CHANNEL MIX CODE", self.codes['mixed_channel'], 'mixed')
        else:
            print(f"\n\n{self.colors['bright_red']}{self.colors['blink']}{self.stickers['cross']} FUSION COLLAPSE! {self.stickers['cross']}{self.colors['reset']}")
            print(f"{self.colors['bright_yellow']}{self.stickers['warning']} RE-ENTER CORRECT CODES!{self.colors['reset']}")
            time.sleep(2)
            self.verify_channel_mix()

    def run(self):
        """Main program loop"""
        # Show epic loading animation
        self.loading_animation()
        
        while self.running:
            try:
                self.show_banner()
                choice = self.main_menu()
                
                if choice == '1':
                    self.filter_codes_menu()
                elif choice == '2':
                    self.show_account_code()
                elif choice == '3':
                    self.show_mixer_code()
                elif choice == '4':
                    self.total_mix_menu()
                elif choice == '5':
                    self.show_github_code_filter()
                elif choice == '6':
                    self.show_how_to_use()
                elif choice == '7':
                    self.exit_sequence()
                    
            except KeyboardInterrupt:
                self.exit_sequence()

    def exit_sequence(self):
        """Epic exit sequence"""
        self.clear()
        
        print(f"\n{self.colors['bright_red']}{self.stickers['skull']}{'💀'*25}{self.stickers['skull']}{self.colors['reset']}")
        self.print_effect(f"{self.colors['bold']}{self.colors['bright_white']}{self.stickers['warning']} SYSTEM SHUTDOWN INITIATED {self.stickers['warning']}{self.colors['reset']}", 
                         effect='glitch', delay=0.05)
        print(f"{self.colors['bright_red']}{self.stickers['skull']}{'💀'*25}{self.stickers['skull']}{self.colors['reset']}\n")
        
        # Countdown with effects
        for i in range(3, 0, -1):
            print(f"{self.colors['blink']}{self.colors['bright_red']}{self.stickers['bomb']} SHUTDOWN IN {i}... {self.stickers['bomb']}{self.colors['reset']}")
            time.sleep(1)
        
        # Goodbye message
        goodbye = f"""
{self.colors['bright_green']}{self.stickers['sparkles']} THANK YOU FOR USING DN FILTER! {self.stickers['sparkles']}
{self.colors['bright_cyan']}{self.stickers['rocket']} POWERED BY ADVANCED ENCRYPTION
{self.colors['bright_yellow']}{self.stickers['crown']} DEVELOPERS: BIGMASOUD & HICHKAS
{self.colors['bright_magenta']}{self.stickers['globe']} SUPPORT: @DN_hackers
{self.colors['bright_red']}{self.stickers['warning']} USE RESPONSIBLY!
{self.colors['bright_white']}{'━'*40}{self.colors['reset']}
"""
        
        for line in goodbye.split('\n'):
            print(line)
            time.sleep(0.1)
        
        self.running = False

def main():
    app = DNFilterUltimate()
    app.run()

if __name__ == "__main__":
    main()
