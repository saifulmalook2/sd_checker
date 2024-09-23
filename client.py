import requests

url = 'http://161.35.127.137:8000/date_check/20 september 2024'
html_content = '''
<div class="ql-editor" data-gramm="false" contenteditable="true">
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
      >DC 1: Company Overview and Types of Products and Services
      Provided</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd is a technology company headquartered in London, UK. The
    company's mission is to democratize financial advice by providing everyone
    globally with an AI Financial Advisor trained by the ablest Advisory
    professionals. This will help people make better financial decisions over
    their lifetime and build sustainable global wealth.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One is an end-to-end advisory process automation platform that learns
    from working with human advisers and replicates tasks that do not require
    personal human interaction.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Its cognitive intelligence (the ‘bot’) streamlines the financial advisory
    processes, unlocking revenue and business growth potential. It enables
    seamless integration with the best advisory tools on the market to deliver
    clients the highest quality and value. The end-to-end unified experience,
    with a single point of digital interaction, strengthens the Financial
    Advisers' brands and reduces cybercrime risk.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The human advisers use the Zenith One ‘skill creator’ through the management
    portal to show the bot how to do things. It is simple, like learning the
    alphabet to spell words.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The human advisor chooses what data needs to be provided, for example,
    retirement advice, how to assess risk, what calculations need to be done and
    when to schedule the initial advisory meeting with the client.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The bot progressively remembers each interaction between the human advisor
    and the client. The activity, the data and what tools to use. Through this,
    it learns how to understand results and, in time, becomes able to deliver
    the process by itself (Autonomous).
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The system described in this report section details the Zenith One Platform.
    Any other Zenith One services are not within the scope of this report.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The Zenith One Platform consists of the following applications:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●The Zenith One Platform consists of the following applications:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Bot building and management portal (manage.zenith.one);
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Web application for advisory firm team members to interact with the bot
    (my.zenith.one);
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Web application for end clients to interact with the bot using the advisory
    firm custom domain and branding.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Web application for managing system configuration (gnosis.zenith.one);
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Identity Provider - web application for managing identities and
    authentication (login.zenith.one)
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)">
    The Zenith One Platform focuses on the following activities:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Workflow automation based on actions and skills,
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Conditional decisions (rules-based, working on the if-then principle),
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Structured and semi-structured data gathering and processing.
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)">
    The bot performs actions from the following categories:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Interaction management: launching new interactions, continuing to
    sub-interactions or continuing new interactions over the interface
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Communication: sending emails or text messages
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Client's data gathering and review from the following data types:
  </p>
  <p style="background-color: rgb(255, 255, 255)">○Personal data</p>
  <p style="background-color: rgb(255, 255, 255)">○Address data</p>
  <p style="background-color: rgb(255, 255, 255)">○Contact details</p>
  <p style="background-color: rgb(255, 255, 255)">○Legal and Compliance data</p>
  <p style="background-color: rgb(255, 255, 255)">
    ○Family and dependents' data
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ○Financial fact-finding, like savings and investments, properties and other
    assets, insurance, debts and more.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Calendar and meetings management: Microsoft Teams or Zoom bookings, office
    meetings or phone calls.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Team management: assigning the team to the interactions, setting
    integrations or performing other back-office tasks
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Use custom forms: multiple choice questions, yes/no, dropdowns, ratings or
    file upload
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Creating and managing Data Vaults that store PII with complete audit trail
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Perform client profiling: risk questionnaires or sustainability
    questionnaires
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Use conditions to make decisions or perform assessments to make a decision
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Create, convert, sign and certify documents
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Use pre-defined components from financial services software suppliers
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Perform legal tasks: gathering consent or declarations
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Structure and translate data, e.g. structure data captured from webhooks or
    forms.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Perform tasks through API interfaces with other financial advisory
    software: asking for client records from back office systems, creating
    clients, synchronizing data one way or two ways, and feeding the
    interactions with data and others.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    There are over 100 different actions and tasks that the bots can perform out
    of the box.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The bot management system allows the financial advisory team's
    administrators and bot designers to manage the bot’s settings:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    the look and feel of the bots, create skills and manage skills, manage
    system messages and compliance, and configure webhooks, triggers and
    connectors to other systems, create document templates that the bot will
    use, create reusable content and semi-structured data sets. The
    administrators can also manage general company-specific settings, like
    company legal data, offices, team members and calendars.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The My Bot application allows the advisory firm team members to interact
    with the bots daily, see and perform assigned tasks, launch new interactions
    with the bot, track the progress, review the data and audit trials. The team
    members can also manage their profiles, connect to external tools and set
    personal preferences for the interactions with the bot.
  </p>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 2: The Principal Service Commitments and System Requirements</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd designs its processes and procedures related to the system to
    meet its objectives. Those objectives are based on the service commitments
    that Zenith One Ltd makes to user entities, the laws and regulations that
    govern the provision of the services, and the financial, operational, and
    compliance requirements that Zenith One Ltd has established for the
    services. The system services are subject to the Security commitments
    established internally for its services.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The Company communicates its commitments to customers through Service Level
    Terms (SLAs), Terms and Conditions (T&amp;Cs), and Privacy Notices.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    <strong style="background-color: rgb(255, 255, 255)"
      >Security commitments</strong
    >
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Security commitments include, but are not limited to, the following:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●System features and configuration settings designed to authorize user
    access while restricting unauthorized users from accessing information not
    needed for their role
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Use of intrusion detection systems to prevent and identify potential
    security attacks from users outside the boundaries of the system
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Regular vulnerability scans over the system and network, and penetration
    tests over the production environment
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Operational procedures for managing security incidents and breaches,
    including notification procedures
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Use of encryption technologies to protect customer data both at rest and in
    transit
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Use of data retention and data disposal
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Up time availability of production systems
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 3: The Components of the System Used to Provide the Services</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    The System is comprised of the following components:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Software - The application programs and IT system software that supports
    application programs (operating systems, middleware, and utilities), the
    types of databases used, the nature of external facing web applications, and
    the nature of applications developed in-house, including details about
    whether the applications in use are mobile applications or desktop or laptop
    applications.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●People - The personnel involved in the governance, operation, security, and
    use of a system (business unit personnel, developers, operators, user entity
    personnel, vendor personnel, and managers).
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Data – The types of data used by the system, such as transaction streams,
    files, databases, tables, and output used or processed by the system.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Procedures – The automated and manual procedures related to the services
    provided, including, as appropriate, procedures by which service activities
    are initiated, authorized, performed, and delivered, and reports and other
    information prepared.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >3.1 Primary Infrastructure</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd maintains a system inventory that includes virtual machines,
    computers(desktops and laptops), and networking devices (switches and
    routers). The inventory documents device name, inventory type, description,
    and owner. To outline the topology of its network, the organization
    maintains the following network diagram(s).
  </p>
  <p style="background-color: rgb(255, 255, 255)">​​</p>
  <table>
    <tbody>
      <tr>
        <td data-row="1"><strong style="color: white">Hardware</strong></td>
        <td data-row="1"><strong style="color: white">Type</strong></td>
        <td data-row="1"><strong style="color: white">Purpose</strong></td>
      </tr>
      <tr>
        <td data-row="2"><span style="color: black">Azure Platform</span></td>
        <td data-row="2"><span style="color: black">Azure</span></td>
        <td data-row="2">
          <span style="color: black"
            >Managed cloud platform where services are hosted</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="3">
          <span style="color: black">Azure Virtual Machine</span>
        </td>
        <td data-row="3"><span style="color: black">Azure</span></td>
        <td data-row="3">
          <span style="color: black"
            >Virtual machine service for web hosting and backend service
            offerings</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="4">
          <span style="color: black">Azure Kubernetes</span>
        </td>
        <td data-row="4"><span style="color: black">Azure</span></td>
        <td data-row="4">
          <span style="color: black"
            >Container orchestration for deployment, scaling, and
            management</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="5"><span style="color: black">Azure Database</span></td>
        <td data-row="5"><span style="color: black">Azure</span></td>
        <td data-row="5">
          <span style="color: black"
            >Transactional database with backups and redundancy</span
          >
        </td>
      </tr>
    </tbody>
  </table>
  <h3><br /></h3>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
    >
      3.2 Primary Software</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd is responsible for managing the development and operation of
    the Zenith One system including infrastructure components such as servers,
    databases, and storage systems. The in-scope Zenith One Ltd infrastructure
    and software components are shown in the table provided below:
  </p>
  <table>
    <tbody>
      <tr>
        <td data-row="1">
          <strong style="color: white">System/Application</strong>
        </td>
        <td data-row="1">
          <strong style="color: white">Operating System</strong>
        </td>
        <td data-row="1"><strong style="color: white">Purpose</strong></td>
      </tr>
      <tr>
        <td data-row="2"><span style="color: black">1password</span></td>
        <td data-row="2"><span style="color: black">N/A</span></td>
        <td data-row="2">
          <span style="color: black"
            >1password Is used as a password manager.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="3">
          <span style="color: black">Allies Computing Ltd (Postcoder)</span>
        </td>
        <td data-row="3"><span style="color: black">N/A</span></td>
        <td data-row="3">
          <span style="color: black"
            >Postcoder is used to validate emails, phone numbers and address
            lookups.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="4"><span style="color: black">Asana</span></td>
        <td data-row="4"><span style="color: black">N/A</span></td>
        <td data-row="4">
          <span style="color: black">Asana is used for task management.</span>
        </td>
      </tr>
      <tr>
        <td data-row="5"><span style="color: black">Cloudflare</span></td>
        <td data-row="5"><span style="color: black">N/A</span></td>
        <td data-row="5">
          <span style="color: black"
            >Cloudflare is used for DNS and traffic management.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="6"><span style="color: black">Exclaimer</span></td>
        <td data-row="6"><span style="color: black">N/A</span></td>
        <td data-row="6">
          <span style="color: black"
            >Exclaimer is used for email signature management.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="7"><span style="color: black">Jira</span></td>
        <td data-row="7"><span style="color: black">N/A</span></td>
        <td data-row="7">
          <span style="color: black"
            >Jira is used for software project management.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="8">
          <span style="color: black">Microsoft Azure</span>
        </td>
        <td data-row="8"><span style="color: black">N/A</span></td>
        <td data-row="8">
          <span style="color: black"
            >Microsoft Azure is used for hosting and running the company’s
            services.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="9"><span style="color: black">Miro</span></td>
        <td data-row="9"><span style="color: black">N/A</span></td>
        <td data-row="9">
          <span style="color: black">Miro is used as a collaboration tool</span>
        </td>
      </tr>
      <tr>
        <td data-row="10"><span style="color: black">Notion</span></td>
        <td data-row="10"><span style="color: black">N/A</span></td>
        <td data-row="10">
          <span style="color: black"
            >Noton is used as a team workspace and wiki.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="11"><span style="color: black">Office 365</span></td>
        <td data-row="11"><span style="color: black">N/A</span></td>
        <td data-row="11">
          <span style="color: black"
            >Office 365 is used for email, phone systems and virtual
            meetings.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="12"><span style="color: black">Pipedrive</span></td>
        <td data-row="12"><span style="color: black">N/A</span></td>
        <td data-row="12">
          <span style="color: black"
            >Pipedrive is used for customer relationship management.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="13"><span style="color: black">Slack</span></td>
        <td data-row="13"><span style="color: black">N/A</span></td>
        <td data-row="13">
          <span style="color: black"
            >Slack is used as the primary communication channel within the
            team.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="14"><span style="color: black">Vanta</span></td>
        <td data-row="14"><span style="color: black">N/A</span></td>
        <td data-row="14">
          <span style="color: black"
            >Vanta is used for compliance management.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="15"><span style="color: black">Zendesk</span></td>
        <td data-row="15"><span style="color: black">N/A</span></td>
        <td data-row="15">
          <span style="color: black"
            >Zendesk is used for customer support.</span
          >
        </td>
      </tr>
    </tbody>
  </table>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >3.3 People</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    The company employs dedicated team members to handle major product
    functions, including operations, and support. The IT/Engineering Team
    monitors the environment, as well as manages data backups and recovery. The
    Company focuses on hiring the right people for the right job as well as
    training them both on their specific tasks and on the ways to keep the
    company and its data secure.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd has a staff of approximately 10 organized in the following
    functional areas:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Management: Individuals who are responsible for enabling other employees to
    perform their jobs effectively and for maintaining security and compliance
    across the environment.
  </p>
  <p style="background-color: rgb(255, 255, 255)">This includes:</p>
  <p style="background-color: rgb(255, 255, 255)">●CEO - Jacek Wojcik</p>
  <p style="background-color: rgb(255, 255, 255)">●CTO - Krzysztof Klein</p>
  <p style="background-color: rgb(255, 255, 255)">
    Operations: Responsible for maintaining the availability of production
    infrastructure, and managing access and security for production
    infrastructure. Only members of the Operations team have access to the
    production environment. Members of the Operations team may also be members
    of the Engineering team.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Information Technology: Responsible for managing laptops, software, and
    other technology involved in employee productivity and business operations.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Product Development: Responsible for the development, testing, deployment,
    and maintenance of the source code for the system. Responsible for the
    product life cycle, including adding additional product functionality.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >3.4 Data</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Data as defined by Zenith One Ltd, constitutes the following:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    User and account data - this includes Personally Identifiable Information
    (PII) and other data from employees, customers, users (customers’
    employees), and other third parties such as suppliers, vendors, business
    partners, and contractors. This collection is permitted under the Terms of
    Service and Privacy Policy (as well as other separate agreements with
    vendors, partners, suppliers, and other relevant third parties). Access to
    PII is controlled through processes for provisioning system permissions, as
    well as ongoing monitoring activities, to ensure that sensitive data is
    restricted to employees based on job function.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Data is categorized in the following major types of data used by Zenith One
    Ltd
  </p>
  <table>
    <tbody>
      <tr>
        <td data-row="1"><strong style="color: white">Category</strong></td>
        <td data-row="1">
          <strong style="color: white">Description</strong>
        </td>
        <td data-row="1"><strong style="color: white">Examples</strong></td>
        <td data-row="1"><br /></td>
        <td data-row="1"><br /></td>
        <td data-row="1"><br /></td>
      </tr>
      <tr>
        <td data-row="2"><span style="color: black">Public</span></td>
        <td data-row="2">
          <span style="color: black"
            >Public information is not confidential and can be made public
            without any implications for Zenith One Ltd.</span
          >
        </td>
        <td data-row="2">●<span style="color: black">Press releases</span></td>
        <td data-row="2">●<span style="color: black">Public website</span></td>
        <td data-row="2"><br /></td>
        <td data-row="2"><br /></td>
      </tr>
      <tr>
        <td data-row="3"><span style="color: black">Internal</span></td>
        <td data-row="3">
          <span style="color: black"
            >Access to internal information is approved by management and is
            protected from external access.</span
          >
        </td>
        <td data-row="3">●<span style="color: black">Internal memos</span></td>
        <td data-row="3">
          ●<span style="color: black">Design documents</span>
        </td>
        <td data-row="3">
          ●<span style="color: black">Product specifications</span>
        </td>
        <td data-row="3">●<span style="color: black">Correspondences</span></td>
      </tr>
      <tr>
        <td data-row="4"><span style="color: black">Customer data</span></td>
        <td data-row="4">
          <span style="color: black"
            >Information received from customers for processing or storage by
            Zenith One Ltd. Zenith One Ltd must uphold the highest possible
            levels of integrity, confidentiality, and restricted availability
            for this information.</span
          >
        </td>
        <td data-row="4">
          ●<span style="color: black">Customer operating data</span>
        </td>
        <td data-row="4">●<span style="color: black">Customer PII</span></td>
        <td data-row="4">
          ●<span style="color: black">Customers' customers' PII</span>
        </td>
        <td data-row="4">
          ●<span style="color: black"
            >Anything subject to a confidentiality agreement with a
            customer</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="5"><span style="color: black">Company data</span></td>
        <td data-row="5">
          <span style="color: black"
            >Information collected and used by Zenith One Ltd to operate the
            business. Zenith One Ltdmust uphold the highest possible levels of
            integrity, confidentiality, and restricted availability for this
            information.</span
          >
        </td>
        <td data-row="5">●<span style="color: black">Legal documents</span></td>
        <td data-row="5">
          ●<span style="color: black">Contractual agreements</span>
        </td>
        <td data-row="5">●<span style="color: black">Employee PII</span></td>
        <td data-row="5">
          ●<span style="color: black">Employee salaries</span>
        </td>
      </tr>
    </tbody>
  </table>
  <p style="background-color: rgb(255, 255, 255)">
    Customer data is managed, processed, and stored in accordance with the
    relevant data protection and other regulations, with specific requirements
    formally established in customer agreements, if any. Customer data is
    captured which is utilized by the company in delivering its services.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    All employees and contractors of the company are obligated to respect and,
    in all cases, to protect customer data.Additionally, Zenith One Ltd has
    policies and procedures in place to proper and secure handling of customer
    data. These policies and procedures are reviewed on at least an annual
    basis.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >3.5 Processes and procedures</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Management has developed and communicated policies and procedures to manage
    the information security of the system. Changes to these procedures are
    performed annually and authorized by management, the executive team, and
    control owners. These procedures cover the following key security life cycle
    areas:
  </p>
  <p style="background-color: rgb(255, 255, 255)">●Physical Security</p>
  <p style="background-color: rgb(255, 255, 255)">●Logical Access</p>
  <p style="background-color: rgb(255, 255, 255)">●Availability</p>
  <p style="background-color: rgb(255, 255, 255)">●Change Control</p>
  <p style="background-color: rgb(255, 255, 255)">●Data Communications</p>
  <p style="background-color: rgb(255, 255, 255)">●Risk Assessment</p>
  <p style="background-color: rgb(255, 255, 255)">●Data Retention</p>
  <p style="background-color: rgb(255, 255, 255)">●Vendor Management</p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h4><br /></h4>
  <h4>
    <strong
      style="color: rgb(79, 129, 189); background-color: rgb(255, 255, 255)"
    >
      3.5.1 Physical security</strong
    >
  </h4>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd’s production servers are maintained by Microsoft Azure. The
    physical and environmental security protections are the responsibility of
    Microsoft Azure. Zenith One Ltd reviews the attestation reports and performs
    a risk analysis of Microsoft Azure on at least an annual basis.
  </p>
  <h4>
    <strong
      style="color: rgb(79, 129, 189); background-color: rgb(255, 255, 255)"
      >3.5.2 Logical access</strong
    >
  </h4>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd provides employees and contracts access to infrastructure via
    a role-based access control system, to ensure uniform, least privilege
    access to identified users and to maintain simple and repartable user
    provisioning and deprovisioning processes.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Access to these systems are split into admin roles, user roles, and no
    access roles. User access and roles are reviewed on a quarterly basis to
    ensure least privilege access.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The Company's Directors and Executives is responsible for provision access
    to the system based on the employee’s role and performing a background
    check. The employee is responsible for reviewing Zenith One Ltd’s policies,
    completing security training. These steps must be completed within 14 days
    of hire.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    When an employee is terminated, Directors is responsible for deprovisioning
    access to all in scope systems within 24 hours for that employee’s
    termination.
  </p>
  <h4>
    <strong
      style="color: rgb(79, 129, 189); background-color: rgb(255, 255, 255)"
      >3.5.3 Computer operations - backups</strong
    >
  </h4>
  <p style="background-color: rgb(255, 255, 255)">
    Customer data is backed up and monitored by the CIO for completion and
    exceptions. If there is an exception, CIO will perform troubleshooting to
    identify the root cause and either rerun the backup or as part of the next
    scheduled backup job.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Backup infrastructure is maintained in Microsoft Azure with physical access
    restricted according to the policies. Backups are encrypted, with access
    restricted to key personnel.
  </p>
  <h4>
    <strong
      style="color: rgb(79, 129, 189); background-color: rgb(255, 255, 255)"
      >3.5.4 Computer operations - availability</strong
    >
  </h4>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd maintains an incident response plan to guide employees on
    reporting and responding to any information security or data privacy events
    or incidents. Procedures are in place for identifying, reporting and acting
    upon breaches or other incidents.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd internally monitors all applications, including the web UI,
    databases, and cloud storage to ensure that service delivery matches SLA
    requirements.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd utilizes vulnerability scanning software that checks source
    code for common security issues as well as for vulnerabilities identified in
    open source dependencies and maintains an internal SLA for responding to
    those issues.
  </p>
  <h4>
    <strong
      style="color: rgb(79, 129, 189); background-color: rgb(255, 255, 255)"
      >3.5.5 Change management</strong
    >
  </h4>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd maintains documented Systems Development Life Cycle (SDLC)
    policies and procedures to guide personnel in documenting and implementing
    application and infrastructure changes. Change
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)">
    control procedures include change request and initiation processes,
    documentation requirements, development practices, quality assurance testing
    requirements, and required approval procedures.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    A ticketing system is utilized to document the change control procedures for
    changes in the application and implementation of new changes. Quality
    assurance testing and User Acceptance Testing (UAT) results are documented
    and maintained with the associated change request. Development and testing
    are performed in an environment that is logically separated from the
    production environment.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Management approves changes prior to migration to the production environment
    and documents those approvals within the ticketing system.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Version control software is utilized to maintain source code versions and
    migrate source code through the development process to the production
    environment. The version control software maintains a history of code
    changes to support rollback capabilities and tracks changes to developers.
  </p>
  <h4>
    <strong
      style="color: rgb(79, 129, 189); background-color: rgb(255, 255, 255)"
      >3.5.6 Data communications</strong
    >
  </h4>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd has elected to use a platform-as-a-service (PaaS) to run its
    production infrastructure in part to avoid the complexity of network
    monitoring, configuration, and operations. The PaaS simplifies our logical
    network configuration by providing an effective firewall around all the
    Zenith One Ltd application containers, with the only ingress from the
    network via HTTPS connections to designated web frontend endpoints.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The PaaS provider also automates the provisioning and deprovisioning of
    containers to match the desired configuration; if an application container
    fails, it will be automatically replaced, regardless of whether that failure
    is in the application or on underlying hardware.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith has implemented a few leading tools for automated source code
    scanning and analyzing, including vulnerability scannings, like Dependabot
    from GitHub, Snyk and SonarQube. An external security audit is performed
    annually. An internal security audit is performed on demand whenever a
    significant change or feature is going to be released.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >3.6 Boundaries of the system</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    The boundaries of the Zenith One are the specific aspects of the Company’s
    infrastructure, software, people,procedures,and data necessary to provide
    its services and that directly supports the services provided to customers.
    Any infrastructure, software, people, procedures, and data that indirectly
    support the services provided to customers are not included within the
    boundaries of the Zenith One One Advisory Process Automation Platform
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    This report does not include the Cloud Hosting Services provided by Azure at
    multiple facilities.
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 4: Disclosures about Identified Security Incidents&nbsp;</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    No significant incidents have occurred to the services provided to user
    entities in the last three months preceding the end of the review date.
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 5: The Applicable Trust Services Criteria and the Related Controls
      Designed to Provide Reasonable Assurance that the Service Organization’s
      Service Commitments and System Requirements were Achieved</strong
    >
  </h2>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.1 Integrity and ethical values</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    The effectiveness of controls cannot rise above the integrity and ethical
    values of the people who create, administer, and monitor them. Integrity and
    ethical values are essential elements of Zenith One Ltd's control
    environment, affecting the design, administration, and monitoring of other
    components. Integrity and ethical behavior are the product of Zenith One
    Ltd's ethical and behavioral standards, how they are communicated, and how
    they are reinforced in practices. They include management’s actions to
    remove or reduce incentives and temptations that might prompt personnel to
    engage in dishonest, illegal, or unethical acts. They also include the
    communication of entity values and behavioral standards to personnel through
    policy statements and codes of conduct, as well as by example.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Specific control activities that the service organization has implemented in
    this area are described below:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Formally, documented organizational policy statements and codes of conduct
    communicate entity values and behavioral standards to personnel.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Policies and procedures require employees sign an acknowledgment form
    indicating they have been given access to the employee manual and understand
    their responsibility for adhering to the policies and procedures contained
    within the manual.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●A confidentiality statement agreeing not to disclose proprietary or
    confidential information, including client information, to unauthorized
    parties is a component of the employee handbook.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Background checks are performed for employees as a component of the hiring
    process.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.2 Commitment to competence</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd's management defines competence as the knowledge and skills
    necessary to accomplish tasks that define employees’ roles and
    responsibilities. Management’s commitment to competence includes
    management’s consideration of the competence levels for jobs and how those
    levels translate into the requisite skills and knowledge.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Specific control activities that the service organization has implemented in
    this area are described below:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Management has considered the competence levels for particular jobs and
    translated required skills and knowledge levels into written position
    requirements.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Training is provided to maintain the skill level of personnel in certain
    positions.
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h3><br /></h3>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
    >
      5.3 Management's philosophy and operating style</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    The Zenith One Ltd management team must balance two competing interests:
    continuing to grow and develop in a cutting edge, rapidly changing
    technology space while remaining excellent and conservative stewards of the
    highly-sensitive data and workflows our customers entrust to us.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The management team meets frequently to be briefed on technology changes
    that impact the way Zenith One Ltd can help customers build data workflows,
    as well as new security technologies that can help protect those workflows,
    and finally any regulatory changes that may require Zenith One Ltd to alter
    its software to maintain legal compliance. Major planned changes to the
    business are also reviewed by the management team to ensure they can be
    conducted in a way that is compatible with our core product offerings and
    duties to new and existing customers.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Specific control activities that the service organization has implemented in
    this area are described below:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Management is periodically briefed on regulatory and industry changes
    affecting the services provided.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Executive management meetings are held to discuss major initiatives and
    issues that affect the business.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.4 Organizational structure and assignment of authority and
      responsibility</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd's organizational structure provides the framework within
    which its activities for achieving entity-wide objectives are planned,
    executed, controlled, and monitored. Management believes establishing a
    relevant organizational structure includes considering key areas of
    authority and responsibility. An organizational structure has been developed
    to suit its needs. This organizational structure is based, in part, on its
    size and the nature of its activities.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd's assignment of authority and responsibility activities
    include factors such as how authority and responsibility for operating
    activities are assigned and how reporting relationships and authorization
    hierarchies are established. It also includes policies relating to
    appropriate business practices, knowledge, and experience of key personnel,
    and resources provided for carrying out duties. In addition, it includes
    policies and communications directed at ensuring personnel understand the
    entity’s objectives, know how their individual actions interrelate and
    contribute to those objectives, and recognize how and for what they will be
    held accountable.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Specific control activities that the service organization has implemented in
    this area are described below:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Organizational charts are in place to communicate key areas of authority
    and responsibility.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Organizational charts are communicated to employees and updated as needed.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.5 HR policies and practices</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd's success is founded on sound business ethics, reinforced
    with a high level of efficiency, integrity, and ethical standards. The
    result of this success is evidenced by its proven track record for hiring
    and retaining top quality personnel who ensures the service organization is
    operating at
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)">
    maximum efficiency. Zenith One Ltd's human resources policies and practices
    relate to employee hiring, orientation, training, evaluation, counseling,
    promotion, compensation, and disciplinary activities.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Specific control activities that the service organization has implemented in
    this area are described below:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●New employees are required to sign acknowledgment forms for the employee
    handbook and a confidentiality agreement following new hire orientation on
    their first day of employment.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Evaluations for each employee are performed on an annual basis.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Employee termination procedures are in place to guide the termination
    process and are documented in a termination checklist.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.6 Risk assessment process</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd’s risk assessment process identifies and manages risks that
    could potentially affect Zenith One Ltd’s ability to provide reliable and
    secure services to our customers. As part of this process, Zenith One Ltd
    maintains a risk register to track all systems and procedures that could
    present risks to meeting the company’s objectives. Risks are evaluated by
    likelihood and impact, and management creates tasks to address risks that
    score highly on both dimensions. The risk register is reevaluated annually,
    and tasks are incorporated into the regular Zenith One Ltd product
    development process so they can be dealt with predictably and iteratively.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.7 Integration with risk assessment</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    The environment in which the system operates; the commitments, agreements,
    and responsibilities of Zenith One Ltd’s system; as well as the nature of
    the components of the system result in risks that the criteria will not be
    met. Zenith One Ltd addresses these risks through the implementation of
    suitably designed controls to provide reasonable assurance that the criteria
    are met. Because each system and the environment in which it operates are
    unique, the combination of risks to meeting the criteria and the controls
    necessary to address the risks will be unique. As part of the design and
    operation of the system, Zenith One Ltd’s management identifies the specific
    risks that the criteria will not be met and the controls necessary to
    address those risks.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.8 Information and communication systems</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Information and communication are an integral component of Zenith One Ltd’s
    internal control system. It is the process of identifying, capturing, and
    exchanging information in the form and time frame necessary to conduct,
    manage, and control the entity’s operations.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd uses several information and communication channels
    internally to share information with management, employees, contractors, and
    customers. Zenith One Ltd uses chat systems and email as the primary
    internal and external communications channels.
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)">
    Structured data is communicated internally via SaaS applications and project
    management tools. Finally, Zenith One Ltd uses in-person and video “all
    hands'' meetings to communicate company priorities and goals from management
    to all employees.
  </p>
  <h3>
    <strong
      style="color: rgb(31, 56, 100); background-color: rgb(255, 255, 255)"
      >5.9 Monitoring controls</strong
    >
  </h3>
  <p style="background-color: rgb(255, 255, 255)">
    Management monitors controls to ensure that they are operating as intended
    and that controls are modified as conditions change. Zenith One Ltd’s
    management performs monitoring activities to continuously assess the quality
    of internal control over time. Necessary corrective actions are taken as
    required to correct deviations from company policies and procedures.
    Employee activity and adherence to company policies and procedures is also
    monitored. This process is accomplished through ongoing monitoring
    activities, separate evaluations, or a combination of the two.
  </p>
  <h4>
    <strong
      style="color: rgb(0, 111, 184); background-color: rgb(255, 255, 255)"
      >5.9.1 On-going Monitoring</strong
    >
  </h4>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd’s management conducts quality assurance monitoring on a
    regular basis and additional training is provided based upon results of
    monitoring procedures. Monitoring activities are used to initiate corrective
    action through department meetings, internal conference calls, and informal
    notifications.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Management’s close involvement in Zenith One Ltd’s operations helps to
    identify significant variances from expectations regarding internal
    controls. Upper management evaluates the facts and circumstances related to
    any suspected control breakdown. A decision for addressing any control’s
    weakness is made based on whether the incident was isolated or requires a
    change in the company’s procedures or personnel. The goal of this process is
    to ensure legal compliance and to maximize the performance of Zenith One
    Ltd’s personnel.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    <strong style="background-color: rgb(255, 255, 255)"
      >Reporting deficiencies</strong
    >
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Our internal risk management tracking tool is utilized to document and track
    the results of on-going monitoring procedures. Escalation procedures are
    maintained for responding and notifying management of any identified risks,
    and instructions for escalation are supplied to employees in company policy
    documents. Risks receiving a high rating are responded to immediately.
    Corrective actions, if necessary, are documented and tracked within the
    internal tracking tool. Annual risk meetings are held for management to
    review reported deficiencies and corrective actions.
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 6: Complementary User Entity Controls (CUECs)</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd’s services are designed with the assumption that certain
    controls will be implemented by user entities. Such controls are called
    complementary user entity controls. It is not feasible for all the Trust
    Services Criteria related to Zenith One Ltd’s services to be solely achieved
    by Zenith One Ltd control procedures. Accordingly, user entities, in
    conjunction with the services, should establish their own internal controls
    or procedures to complement those of Zenith One Ltd’s.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The following complementary user entity controls should be implemented by
    user entities to provide additional assurance that the Trust Services
    Criteria described within this report are met. As these items represent only
    a part of the control considerations that might be pertinent at the user
    entities’ locations, user entities’ auditors should exercise judgment in
    selecting and reviewing these complementary user entity controls.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●User entities are responsible for understanding and complying with their
    contractual obligations to Zenith One Ltd.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●User entities are responsible for notifying Zenith One Ltd of changes made
    to technical or administrative contact information.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●User entities are responsible for maintaining their own system(s) of
    record.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●User entities are responsible for ensuring the supervision, management, and
    control of the use of Zenith One Ltd services by their personnel.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●User entities are responsible for developing their own disaster recovery
    and business continuity plans that address the inability to access or
    utilize Zenith One Ltd services.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●User entities are responsible for providing Zenith One Ltd with a list of
    approvers for security and system configuration changes for data
    transmission.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●User entities are responsible for immediately notifying Zenith One Ltd of
    any actual or suspected information security breaches, including compromised
    user accounts, including those used for integrations and secure file
    transfers.
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 7: Complementary Subservice Organization Controls (CSOCs)</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    This report does not include the Cloud Hosting Services provided by Azure at
    multiple facilities.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The Cloud Hosting Services provided by Azure support the physical
    infrastructure of the entities services.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd’s services are designed with the assumption that certain
    controls will be implemented by subservice organizations. Such controls are
    called complementary subservice organization controls. It is not feasible
    for all of the trust services criteria related to Zenith One Ltd’s services
    to be solely achieved by Zenith One Ltd control procedures.Accordingly,
    subservice organizations, in conjunction with the services, should establish
    their own internal controls or procedures to complement those of Zenith One
    Ltd.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    The following subservice organization controls have been implemented by
    Microsoft Azure and included in this report to provide additional assurance
    that the trust services criteria are met.
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    <strong style="background-color: rgb(255, 255, 255)">Azure </strong>
  </p>
  <table>
    <tbody>
      <tr>
        <td data-row="1"><strong style="color: white">Category</strong></td>
        <td data-row="1"><strong style="color: white">Criteria</strong></td>
        <td data-row="1"><strong style="color: white">Control</strong></td>
      </tr>
      <tr>
        <td data-row="2"><span style="color: black">Security</span></td>
        <td data-row="2"><span style="color: black">CC 6.4</span></td>
        <td data-row="2">
          <span style="color: black"
            >Procedures to restrict physical access to the datacenter to
            authorized employees, vendors, contractors, and visitors, have been
            established.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="3"><span style="color: black">Security</span></td>
        <td data-row="3"><span style="color: black">CC 6.4</span></td>
        <td data-row="3">
          <span style="color: black"
            >Security verification and check-in for personnel requiring
            temporary access to the interior of the datacenter facility,
            including tour groups or visitors, are required.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="4"><span style="color: black">Security</span></td>
        <td data-row="4"><span style="color: black">CC 6.4</span></td>
        <td data-row="4">
          <span style="color: black"
            >Physical access to the datacenter is reviewed quarterly and
            verified by the Datacenter Management team.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="5"><span style="color: black">Security</span></td>
        <td data-row="5"><span style="color: black">CC 6.4</span></td>
        <td data-row="5">
          <span style="color: black"
            >Physical access mechanisms (e.g., access card readers, biometric
            devices, man traps / portals, cages, locked cabinets) have been
            implemented and are administered to restrict access to authorized
            individuals.</span
          >
        </td>
      </tr>
      <tr>
        <td data-row="6"><span style="color: black">Security</span></td>
        <td data-row="6"><span style="color: black">CC 6.4</span></td>
        <td data-row="6">
          <span style="color: black"
            >The datacenter facility is monitored 24x7 by security
            personnel.</span
          >
        </td>
      </tr>
    </tbody>
  </table>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)">
    Zenith One Ltd management, along with the subservice provider, define the
    scope and responsibility of the controls necessary to meet all the relevant
    trust services criteria through written contracts, such as service level
    agreements.In addition, Zenith One Ltd performs monitoring of the subservice
    organization controls, including the following procedures:
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Reviewing and reconciling output reports
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Holding periodic discussions with vendors and subservice organization(s)
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Making regular site visits to vendor and subservice organization(s’)
    facilities
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Testing controls performed by vendors and subservice organization(s)
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Reviewing attestation reports over services provided by vendors and
    subservice organization(s)
  </p>
  <p style="background-color: rgb(255, 255, 255)">
    ●Monitoring external communications, such as customer complaints relevant to
    the services by the subservice organization
  </p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 8: Any Specific Criterion of the Applicable Trust Services Criteria
      that is Not Relevant to the System and the Reasons it is Not
      Relevant</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    All Security criteria were applicable to the Zenith One Ltd's Zenith One
    system.
  </p>
  <h2><br /></h2>
  <p style="background-color: rgb(255, 255, 255)"><br /></p>
  <h2><br /></h2>
  <h2><br /></h2>
  <h2>
    <strong
      style="color: rgb(11, 83, 148); background-color: rgb(255, 255, 255)"
    >
      DC 9: Disclosures of Significant Changes In Last 1 Year</strong
    >
  </h2>
  <p style="background-color: rgb(255, 255, 255)">
    No significant changes have occurred to the services provided to user
    entities in the last three months preceding the end of the review date.
  </p>
</div>
<div class="ql-tooltip ql-hidden">
  <a class="ql-preview" target="_blank" href="about:blank"></a
  ><input
    type="text"
    data-formula="e=mc^2"
    data-link="https://quilljs.com"
    data-video="Embed URL"
  /><a class="ql-action"></a><a class="ql-remove"></a>
</div>

'''

response = requests.post(url, data=html_content, headers={'Content-Type': 'text/html'})
print(response.json())
