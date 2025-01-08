#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:01:01 2025

@author: N. Anderson
"""

import random
import pygame
import sys
import os  # Import os for dynamic path handling

# Initialize pygame
pygame.init()

# Screen size
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Rock-Paper-Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Dynamic path for the Assets folder
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
assets_dir = os.path.join(base_dir, "Assets")  # Define the Assets directory

# Game options and images
options = ("rock", "paper", "scissors")
images = {
    "rock": pygame.image.load(os.path.join(assets_dir, "rock.png")),
    "paper": pygame.image.load(os.path.join(assets_dir, "paper.png")),
    "scissors": pygame.image.load(os.path.join(assets_dir, "scissors.png")),
}

# Scale images (optional)
images = {key: pygame.transform.scale(img, (100, 100)) for key, img in images.items()}

# Game state
player_choice = None
computer_choice = None
message = "Make your choice!"
player_wins = 0
rounds = 7
current_round = 1
game_over = False


# Function to draw text on screen
def draw_text(text, x, y, color=WHITE):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))


# Main game loop
running = True
while running:
    screen.fill(BLACK)  # Set background color to black

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Detect button clicks for rock, paper, scissors
            if 50 <= x <= 150 and 300 <= y <= 350:
                player_choice = "rock"
            elif 200 <= x <= 300 and 300 <= y <= 350:
                player_choice = "paper"
            elif 350 <= x <= 450 and 300 <= y <= 350:
                player_choice = "scissors"

            # Detect click on Exit button
            if 600 <= x <= 680 and 10 <= y <= 50:
                pygame.quit()
                sys.exit()

            if game_over and 200 <= x <= 400 and 360 <= y <= 400:
                player_wins = 0
                current_round = 1
                game_over = False
                message = "Make your choice!"
                player_choice = None
                computer_choice = None

            if player_choice:
                # Computer makes a random choice
                computer_choice = random.choice(options)

                # Determine the result
                if player_choice == computer_choice:
                    message = f"Round {current_round}: It's a tie!"
                elif (player_choice == "rock" and computer_choice == "scissors") or \
                     (player_choice == "paper" and computer_choice == "rock") or \
                     (player_choice == "scissors" and computer_choice == "paper"):
                    message = f"Round {current_round}: You win!"
                    player_wins += 1
                else:
                    message = f"Round {current_round}: You lose!"

                current_round += 1

                # Check if the game is over
                if current_round > rounds:
                    game_over = True
                    message += f" Final Score: {player_wins}/{rounds}"

    # Draw UI elements
    draw_text(f"Rock-Paper-Scissors", 180, 20, CYAN)
    draw_text(f"Round: {current_round}/{rounds}", 50, 80)  # Repositioned round score
    draw_text(f"Score: {player_wins}", 500, 80)

    # Draw buttons
    pygame.draw.rect(screen, BLACK, (50, 300, 100, 50))  # Rock
    draw_text("Rock", 70, 310, WHITE)
    pygame.draw.rect(screen, BLACK, (200, 300, 100, 50))  # Paper
    draw_text("Paper", 220, 310, WHITE)
    pygame.draw.rect(screen, BLACK, (350, 300, 120, 50))  # Scissors
    draw_text("Scissors", 360, 310, WHITE)

    # Show choices
    if player_choice:
        # Display player and computer choices as images
        screen.blit(images[player_choice], (100, 120))  # Adjusted player image position
        screen.blit(images[computer_choice], (400, 120))  # Adjusted computer image position
        draw_text("Player", 120, 240, WHITE)  # Adjusted player label
        draw_text("Computer", 420, 240, WHITE)  # Adjusted computer label

    # Restart option
    if game_over:
        pygame.draw.rect(screen, RED, (200, 360, 200, 40))
        draw_text("Restart Game", 230, 370, WHITE)

    # Draw Exit Button
    pygame.draw.rect(screen, CYAN, (600, 10, 80, 40))  # Exit button position
    draw_text("Exit", 620, 20, BLACK)  # Label for Exit button

    pygame.display.update()

pygame.quit()
sys.exit()
