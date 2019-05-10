%% This script applies a random policy on a constant game
clc;
close; 
clear all;

%% Get both games

game_1 = gameLookupTable('./data/univLatencies.mat',      1); % website
game_2 = gameLookupTable('./data/plannerPerformance.mat', 1); % planar
game_actual = gameLookupTable('game', 1); % this is the actual one that will be played

%% Define actions and rounds from both games
global Actions_1
global Actions_2
Actions_1 = game_1.nbActions;
Actions_2 = game_2.nbActions;
rounds_1 = game_1.totalRounds;
rounds_2 = game_2.totalRounds;
%[a,s] = size(rounds_2);
%disp([a,s]);

%% Define the indeces of seperation
global seperation_of_games;
seperation_of_games = [ones(rounds_1, 1);   %1861
    ones(rounds_2, 1) *2 ];                %   1
%[a,s] = size(seperation_of_games);
%disp(a);
%disp(s);
%% Merge the actions and rounds for both games
game_actual.nbActions = Actions_1 + Actions_2;
game_actual.totalRounds = rounds_1 + rounds_2;

% Define the updated table of rewards
g1_R = game_1.tabR;
g2_R = game_2.tabR;
r_choice = randperm( rounds_1 + rounds_2 );        % Randomply permutate betwen rounds
disp(r_choice);
game_actual.tabR = game_actual.tabR( :, r_choice');        % Define this permutated choice reward table

% Filling missing data in this table with ones.
% This occurs for nbActions of one game, combined with the totalRounds of
% the other, this doesn't exist so one the elements in this matrix region
unknown_1 = ones(Actions_1, rounds_2);
unknown_2 = ones(Actions_2, rounds_1);

% Here now the define the table of rewards for the actual game you are playin
% which comebines both games
game_actual.tabR = [g1_R, unknown_1;
    unknown_2, g2_R];

%game_actual.N = 0;
% Shuffle tabR choice of round around
seperation_of_games = seperation_of_games(r_choice);    


%% Get a set of policies to try out
policies = {policyEXP3(), policyUCB(),policyRandom()};
policy_names = {'policyEXP3', 'policyUCB','policyRandom'};

%% Run the policies on the game
figure;
hold on;
for k = 1:length(policies)
    policy = policies{k};
    game_actual.resetGame();
    [reward, action, regret] = game_actual.play(policy);
    fprintf('Policy: %s Reward: %.2f\n', class(policy), sum(reward));
    %plot(regret);
    % or scatter plot of actions
    [x,y] = size(action);
    % Display the actions
    scatter(1:y, action, 3);
end
legend(policy_names);

