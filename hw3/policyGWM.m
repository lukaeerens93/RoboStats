classdef policyGWM < Policy
    %POLICYGWM This policy implementes GWM for the bandit setting.
    
    properties
        nbActions % number of bandit actions
        
        % Add more member variables as needed
        counter
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
            % Initialize any member variables
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
            % Choose an action according to multinomial distribution
            action = random(makedist('Multinomial', 'probabilities', self.prob), 1, 1);
            self.action = action;
        end
        
        function getReward(self, reward)
            nbA = self.nbActions;
            LA = self.lastAction;
            
            % Update the weights
            %       1) find eta
            log_actions = log(nbA);
            avg_log_actions = log_actions / self.counter;
            self.eta = avg_log_actions^.5;
            
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
            self.lossVector = zeros(1, nbA);
            loss_ = self.lossScalar;
            self.lossVector(LA) = loss_;
            
            % Do more stuff here using loss Vector
            
            % Step through and increment for next loop
            self.lastAction = self.action;
            self.counter = self.counter + 1;
        end        
    end
end

