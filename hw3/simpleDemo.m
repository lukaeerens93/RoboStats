%% This script applies a random policy on a constant game
clc;
close; 
clear all;

%{
%% Get the constant game
game = gameConstant();
%game = gameGaussian(10, 10000);
%game = gameAdversarial(2, 1000);

%% Get a set of policies to try out
policies = {policyConstant(), policyRandom(), policyGWM(), policyEXP3};
policy_names = {'policyConstant', 'policyRandom', 'policyGWM', 'policyEXP3'};

%policies = {policyUCB(), policyEXP3()};
%policy_names = {'policyUCB', 'policyEXP3'};

%policies = {policyEXP3()};
%policy_names = {'policyEXP3'};
%% Run the policies on the game
figure;
hold on;
for k = 1:length(policies)
    disp(k);
    policy = policies{k};
    game.resetGame();
    [reward, action, regret] = game.play(policy);
    fprintf('Policy: %s Reward: %.2f\n', class(policy), sum(reward));
    plot(regret);
    %plot(reward);
    [histo,y] = size(action);
    % Display the actions
    %scatter(1:y, action, 3);

end
legend(policy_names);
%}

%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This section below is for question 5...

%% Get the constant game

% For the website dataset
game = gameLookupTable('./data/univLatencies.mat', 1);

% For the planar dataset
% game = gameLookupTable('./data/plannerPerformance.mat', 1);

%% Get a set of policies to try out
policies = {policyEXP3(), policyUCB(),policyRandom()};
policy_names = {'policyEXP3', 'policyUCB','policyRandom'};
%policies = {policyRandom()};
%policy_names = {'policyRandom'};

%% Run the policies on the game
figure;
hold on;
for k = 1:length(policies)
    policy = policies{k};
    game.resetGame();
    [reward, action, regret] = game.play(policy);
    fprintf('Policy: %s Reward: %.2f\n', class(policy), sum(reward));
    %plot(regret);
    % or scatter plot of actions
    [x,y] = size(action);
    % Display the actions
    scatter(1:y, action, 3);
end
legend(policy_names);
%%
