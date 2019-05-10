classdef policyEXP3 < Policy
    %POLICYEXP3 This is a concrete class implementing EXP3.
    
    properties
        % Define member variables
        % Add more member variables as needed
        counter
        nbActions
        % These are more associated with the weight update
        eta
        weights
        prob
        
        % These are used for everything else
        lossScalar
        action
        lastAction
        lossVector
    end
    
    methods

        function init(self, nbActions)
            % Initialize member variables
            % Same initializations as the policyGWM
            self.nbActions = nbActions;
            
            % Initialize other variables as needed
            self.counter = 1;
            
            self.eta = (log(self.nbActions)/self.counter)^.5;
            self.weights = ones(nbActions,1);
            self.prob = self.weights/sum(self.weights);
            
            self.lossScalar = 0;
            self.action = 1;
            self.lastAction = 1;
            self.lossVector = zeros(1,self.nbActions);    
        end
        
        function action = decision(self)
            % Choose an action
            % Same mumbo jumbo as policyGWM
            action = random(makedist('Multinomial', 'probabilities', self.prob), 1, 1);
            self.action = action;
        end
        
        function getReward(self, reward)
            % Everything is the f*****g same as policyGWM, except loss and
            % eta now need to factor the number of actions
            
            % reward is the reward of the chosen action
            % update internal model
            nbA = self.nbActions;
            LA = self.lastAction;
            % Update the weights
            %       1) find eta
            log_actions = log(nbA);
            avg_log_actions = log_actions / self.counter;
            % Now we also need to average based on the number of actions
            avg_avg = avg_log_actions / nbA; 
            self.eta = avg_avg^.5;
            
            %       2) find weights
            % You are exponentiating the weights with each update you goon
            % What is the exponent function? Here it is:
            e_func = self.eta * self.lossScalar;
            e = exp(-e_func);
            self.weights(LA) = self.weights(LA)*e;
            
            %       3) find probabilities
            self.prob = self.weights / sum(self.weights);
            
            % First we create the loss vector for GWM
            self.lossScalar = 1 - reward;
            self.lossVector = zeros(1,nbA);
            % Now the loss needs to be averaged based on the number of
            % actions available
            loss_ = self.lossScalar/ nbA;
            self.lossVector(LA) = loss_;
            
            % Do more stuff here using loss Vector
            
            % Step through and increment for next loop
            self.lastAction = self.action;
            self.counter = self.counter + 1;
        end        
    end
end