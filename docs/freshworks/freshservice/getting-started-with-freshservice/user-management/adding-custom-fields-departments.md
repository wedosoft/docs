# Adding Custom Fields for Requester Departments

Different organizations have their own unique structure for their departments and related functions. Since each department is usually structured differently, a single set of generic fields may not be sufficient to describe a department. Agents often handle incidents and service requests specific to a department and would require more context to resolve the issue effectively.

**Department Fields in Freshservice** introduces more flexibility and enables customization in defining departments and thus provides additional context to agents regarding the incident or service request from a particular department.

## Key use cases for adding custom fields

Some of the use cases that would entail the use of custom fields for departments:

- **Extended department descriptions:** A service desk admin might need to extend existing department descriptions through custom fields to accommodate new details from a raised incident.

- **Tool integration mapping:** An admin might be required to map company details from different tools (for example a CRM tool) into the service desk in order to have a consistent view of a particular set of entities across a spectrum of tools that are being utilized.

- **Acquired organization support:** An admin might need to introduce new custom fields for departments of an acquired organization.

- **Compliance requirements:** In order to meet specific compliance or regulatory norms, an admin might need to introduce new custom fields to existing departments.

## A quick guide to adding custom department fields or company fields (if you are an MSP)

### Step 1: Access Admin Console

1. **Login to Freshservice** as an Admin.

2. Go to the **Admin console** and click on **Departments Fields**.
   - If your account has more than one workspace, navigate to **Admin > Global Settings > User management > Department Fields**.

### Step 2: Select Field Type

Select the required field type from the following options:

- **Single Line Text**
- **Multi-Line Text**
- **Checkbox**
- **Number**
- **Dropdown**
- **Phone Number**
- **URL**
- **Date**

### Step 3: Add Field to Form

You can **drag and drop** a field type to the form or just **click and position** it later.

### Step 4: Configure Field Properties

1. After choosing the required field type, enter its **label**.

2. If the field should be made mandatory, enable the **"required when submitting the form"** checkbox.

### Step 5: Configure Dropdown Options (if applicable)

In case you are utilizing the **Dropdown** option, you can provide multiple choices.

### Step 6: Save Configuration

After you've added all the required fields, click **Done** and then click **Save**.

## Important Notes

- The newly added field(s) will be **available across departments/companies**.
- In an **analytics data export**, only the Department Name field is available along with the Department's Last updated date and the Department Created date.

## FAQ's

### 1) Can we add multiple department heads while creating a department in Freshservice?

By default, we can add only **one department Head**. Having multiple department heads for a single department could potentially create confusion or complications in terms of accountability and decision-making. To enforce a standard practice where each department has a designated head, Freshservice allows only one head per department.

## Best Practices

- **Plan your custom fields** before implementation to ensure they meet your organizational needs
- **Use clear, descriptive labels** for custom fields to improve user experience
- **Consider mandatory vs optional fields** carefully to balance data collection with user convenience
- **Regular review** of custom fields to ensure they remain relevant and useful
- **Document field purposes** for future reference and onboarding of new administrators