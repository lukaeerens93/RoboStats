classdef policyUCB < Policy
    %POLICYUCB This is a concrete class implementing UCB.

    properties
        % Member variables
        nbActions
        counter
        % Other variables that
        a               % alpha
        loss            % loss of the learner
        action          % action taken
              
        S   % Si <-- 0 for all i from {1, ... , N}
        C   % Ci <-- 0 for all i from {1, ... , N}
        % where N is the total number of actions
    end
    
    methods
        
        function init(self, nbActions)
            % Initialize
            self.nbActions = nbActions;
            % Used to make the waffle afterwards less verbose
            nbA = nbActions;    
            
            % Initialize other variables as needed
            self.counter = 1;
            self.a       = 1;
            self.action  = 1;
            self.loss    = 0;
            
            % Initialize other variables as needed
            self.S = zeros(nbA, 1);
            self.C = zeros(nbA, 1);
        end
        
        
        function action = decision(self)
            global matrix_of_a_t;
            nbA   = self.nbActions;
            s     = self.S;
            c     = self.C;
            alpha = self.a;
            cntr  = self.counter;

            % Explore all arms
            if (nbA >= cntr)
                % Pick action
                action = cntr;
            end
            
            % Exploit best arm
            if (nbA < cntr)
                numerator   = alpha*log(cntr);
                denominator = 2.* c;
                func        = numerator./denominator;
                sqrt_func   = func.^0.5;
                a_t         = s./c + sqrt_func;
                
                % Find index of largest a_t
                [~ , indx_max] = max(a_t);
                action         = indx_max;  % Pick action
                
                % Append a_t to a container 
                matrix_of_a_t = [matrix_of_a_t, a_t];
            end
            
            % Update in class
            self.action  = action;
            % Increment the counter
            self.counter = self.counter + 1;
        end
        
        
        function getReward(self, reward)
            % gta <-- GetReward()
            % In this case the loss is expressed as the reward
            self.loss = reward;
            s_a       = self.action; 
            s         = self.S;
            c         = self.C;
            
            % Update s and c
            s(s_a)    = s(s_a) + reward;
            c(s_a)    = c(s_a) + 1;
        end        
    end

end
